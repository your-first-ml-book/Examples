from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import sys
from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
FLAGS = None

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial, name='weights')
    
def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial, name='bias')
    
def conv2d(x, W):
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding='SAME', name='conv')

def max_pool_2x2(x):
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1],strides=[1, 2, 2, 1], padding='SAME', name='pool')

def main(_):
    # 데이터를 읽어 들입니다.
    mnist = input_data.read_data_sets(FLAGS.data_dir, one_hot=True)
    
    x = tf.placeholder(tf.float32, [None, 784],name='x')
    y_ = tf.placeholder(tf.float32, [None, 10])
    
    with tf.name_scope('first_conv'):
        W_conv1 = weight_variable([5, 5, 1, 32])
        b_conv1 = bias_variable([32])
        x_image = tf.reshape(x, [-1, 28, 28, 1])
        h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1,name='act')

    with tf.name_scope('first_pool'):
        h_pool1 = max_pool_2x2(h_conv1)
    
    with tf.name_scope('second_conv'):
        W_conv2 = weight_variable([5, 5, 32, 64])
        b_conv2 = bias_variable([64])
        h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2,name='act')
    
    with tf.name_scope('second_pool'):
        h_pool2 = max_pool_2x2(h_conv2)

    with tf.name_scope('first_fc'):
        W_fc1 = weight_variable([7 * 7 * 64, 1024])
        b_fc1 = bias_variable([1024])
        h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 * 64])
        h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1,name='act')
    
    with tf.name_scope('drop_out'):
        keep_prob = tf.placeholder(tf.float32)
        h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)
        
    with tf.name_scope('second_fc'):
        W_fc2 = weight_variable([1024, 10])
        b_fc2 = bias_variable([10])
        y_conv = tf.matmul(h_fc1_drop, W_fc2) + b_fc2
    
    cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(y_conv, y_),name='cross_ent')
    train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
    
    correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    
    
    # 그래프 구조를 기록하기 위한 폴더
    logdir = './deep_graph'
    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        # 텐서보드 기록용
        summary_writer = tf.summary.FileWriter(logdir, sess.graph)

        for i in range(10000):
            # 한 번에 데이터 100개를 이용하여 학습합니다.
            batch = mnist.train.next_batch(100)
            if i % 100 == 0:
                # 평가 시에는 완성된 모델을 사용하기 위해
                # 드롭-아웃을 하지 않으므로 keep_prob가 1.0이 됩니다.
                train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_: batch[1], keep_prob: 1.0})
            print("step %d, training accuracy %g" % (i, train_accuracy))
            train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})
         print("test accuracy %g" % accuracy.eval(feed_dict={x: mnist.test.images,y_: mnist.test.labels, keep_prob: 1.0}))
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--data_dir', type=str,default='/tmp/tensorflow/mnist/input_data',help='Directory for storing input data')
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)
