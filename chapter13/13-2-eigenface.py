import cv2
import numpy as np
import sys
from sklearn.model_selection import train_test_split 
from sklearn.metrics import classification_report 
from sklearn.decomposition import PCA
from sklearn.model_selection import GridSearchCV 
from sklearn.svm import SVC

def read_data(fin):
    ''' 이미지 파일을 읽어 들여 이미지 데이터, 이미지 얼굴 번호, 사람 이름을 리턴합니다. fin 파일은 각 이미지 데이터의 경로를 포함하고 있습니다.
    '''
    target_li = []
    data_li = []
    for line in open(fin):
        image_path, face_id = line.strip().split(';') 
        target_name = image_path.split('/')[1]
        image_data = cv2.imread(image_path, cv2.COLOR_BGR2GRAY)
        data_li.append(image_data) # 이미지 데이터 
        target_li.append(int(face_id)) # 이미지 얼굴 번호
    return(np.array(data_li), np.array(target_li))


def create_train_test_data(image_data, label_li):
    
    # 이미지데이터수,이미지세로픽셀크기,이미지가로픽셀크기 
    n_samples, image_h, image_w = image_data.shape
    # 가로 픽셀 강도벡터와 세로 픽셀 강도벡터를 이어서 하나의 벡터로 만듭니다. 
    # 길이는 image_h x image_w가 되겠죠. 그리고 이 벡터가 피처 벡터가 됩니다. 
    X = image_data.reshape(n_samples, -1)
    n_features = X.shape[1] # 피처 크기
    y = label_li # 학습 레이블
    
    n_classes = len(set(y)) # 클래스(인물) 수
    print("Total dataset size:") 
    print("n_samples: %d" % n_samples) 
    print("n_features: %d" % n_features) 
    print("n_classes: %d" % n_classes)
    # 사이킷런의 함수 train_test_split을 이용하여 학습셋과 평가셋을 나눕니다. 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    return(X_train, X_test, y_train, y_test)

def extract_features(X_train, X_test, n_components): 
    print("Extracting the top %d eigenfaces from %d faces"% (n_components, X_train.shape[0])) 
    pca = PCA(n_components=n_components,svd_solver='randomized', whiten=True).fit(X_train) 
    X_train_pca = pca.transform(X_train)
    X_test_pca = pca.transform(X_test) 
    return(X_train_pca, X_test_pca)

def train_test_classifer(X_train_pca, X_test_pca, y_train, y_test): 
    print("Fitting the classifier to the training set")
    param_grid = {'C': [1e3, 5e3, 1e4, 5e4, 1e5],'gamma': [0.0001, 0.0005, 0.001, 0.005, 0.01, 0.1]}
    clf = GridSearchCV(SVC(kernel='rbf', class_weight='balanced'), param_grid) 
    clf = clf.fit(X_train_pca, y_train)
    print("Best estimator found by grid search:")
    print(clf.best_estimator_)
    
    print("Predicting people's names on the test set") 
    y_pred = clf.predict(X_test_pca) 
    print(classification_report(y_test, y_pred))
    
if __name__ == '__main__': 
    argv = sys.argv
    image_data, label = read_data('faces.csv')
    n_eigenface = 10 # 추출할 고유 얼굴 수
    X_train, X_test, y_train, y_test = create_train_test_data(image_data, label) 
    X_train_pca, X_test_pca = extract_features(X_train, X_test, n_eigenface) 
    train_test_classifer(X_train_pca, X_test_pca, y_train, y_test)
