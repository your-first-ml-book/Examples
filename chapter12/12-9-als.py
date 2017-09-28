from sklearn.metrics import mean_squared_error
import numpy as np
def compute_ALS(R, n_iter, lambda_, k):
    '''임의의 사용자 요인 행렬 X와 임의의 영화 요인 행렬 Y를 생성한 뒤
    교대 최소제곱법을 이용하여 유틸리티 행렬 R을 근사합니다.
    R(ndarray) : 유틸리티 행렬
    lambda_(float) : 정규화 파라미터입니다.
    n_iter(fint) : X와 Y의 갱신 횟수입니다.
    '''
    m, n =R.shape
    X = np.random.rand(m, k)
    Y = np.random.rand(k, n)

    # 각 갱신 때마다 계산한 에러를 저장합니다.
    errors =[]
    for i in range(0, n_iter):
        # [식 6-4]를 구현했습니다.
        # 넘파이의 eye 함수는 파라미터 a를 받아 a x a 크기의 단위행렬을 만듭니다.
        X = np.linalg.solve(np.dot(Y, Y.T) + lambda_ * np.eye(k), np.dot(Y, R.T)).T
        Y = np.linalg.solve(np.dot(X.T, X) + lambda_ * np.eye(k), np.dot(X.T, R))
        
        errors.append(mean_squared_error(R, np.dot(X, Y)))
        
        if i % 10 == 0:
            print('iteration %d is completed'%(i))
            #print(mean_squared_error(R, np.dot(X, Y)))
        
    R_hat = np.dot(X, Y)
    print('Error of rated movies: %.5f'%(mean_squared_error(R, np.dot(X, Y))))
    return(R_hat, errors)
