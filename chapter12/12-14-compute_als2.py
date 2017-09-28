from sklearn.metrics import mean_squared_error
import numpy as np

def compute_ALS2(R, test, n_iter, lambda_, k):
    '''임의의 사용자 요인 행렬 X와 임의의 영화 요인 행렬 Y를 생성하고 교대 최소제곱법을 이용하여
    유틸리티 행렬 R을 근사합니다. 그후 test행렬을 이용하여 평가합니다.
    R(ndarray) : 유틸리티 행렬
    test: 평가행렬
    lambda_(float) : 정규화 파라미터
    n_iter(fint) : X와 Y의 갱신 횟수
    '''
    m,n =R.shape
    X = np.random.rand(m, k)
    Y = np.random.rand(k, n)
    errors =[]
    # 갱신 시마다 계산한 에러를 저장합니다.
    for i in range(0, n_iter):
        X = np.linalg.solve(np.dot(Y, Y.T) + lambda_ * np.eye(k),np.dot(Y, R.T)).T
        Y = np.linalg.solve(np.dot(X.T, X) + lambda_ * np.eye(k), np.dot(X.T, R))
        errors.append(get_test_mse(test,np.dot(X, Y)))

        if i % 10 == 0:
            print('iteration %d is completed'%(i))
    
    R_hat = np.dot(X, Y)
    print('Error of rated movies: %.5f'%(get_test_mse(test,R_hat)))
    return(R_hat, errors)
