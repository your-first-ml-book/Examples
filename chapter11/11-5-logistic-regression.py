import pickle
from sklearn.linear_model import LogisticRegression

with open('processed.pickle', 'rb') as file_handle:
    vocabulary, features, labels = pickle.load(file_handle)

# 학습-평가 데이터 나누기
# 처음 50%를 학습으로 사용하고 나머지를 평가로 사용합니다.
total_number = len(labels)
middle_index = total_number//2
train_features = features[:middle_index,:]
train_labels = labels[:middle_index]
test_features = features[middle_index:,:]
test_labels = labels[middle_index:]

classifier = LogisticRegression()
classifier.fit(train_features, train_labels)
print('train accuracy: %4.4f' % classifier.score(train_features, train_labels))
print('test accuracy: %4.4f' % classifier.score(test_features, test_labels))

# 어떤 항목이 판별에 영향을 많이 줬는지 찾아보기
weights = classifier.coef_[0, :]
pairs = []
for index, value in enumerate(weights):
    pairs.append( (abs(value), vocabulary[index]) )
pairs.sort(key=lambda x: x[0], reverse=True)
for pair in pairs[:20]:
    print('score %4.4f word: %s' % pair)
