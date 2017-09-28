W = R>0.0
W[W == True] = 1
W[W == False] = 0
W = W.astype(np.float64, copy=False)

def compute_wALS(R,W, n_iter, lambda_, k):
    m,n = R.shape
    X = np.random.rand(m, k)
    Y = np.random.rand(k, n)
    weighted_errors = []
    
    # [예제 12-9]와 달리 가중치 행렬을 넣어서 계산합니다.
    for ii in range(n_iter):
        # 각 사용자와 영화의 가중치 행렬을 이용하여 X와 Y를 갱신합니다.
        for u, Wu in enumerate(W):
            X[u,:] = np.linalg.solve(np.dot(Y, np.dot(np.diag(Wu), Y.T)) +lambda_ * np.eye(k), np.dot(Y, np.dot(np.diag(Wu),R[u,:].T))).T
        for i, Wi in enumerate(W.T):
            Y[:, i] = np.linalg.solve(np.dot(X.T, np.dot(np.diag(Wi), X)) + lambda_ * np.eye(k), np.dot(X.T, np.dot(np.diag(Wi), R[:, i])))

        # 가중치 행렬을 mean_squared_error 함수의 인자로 사용합니다.
        weighted_errors.append(mean_squared_error(R, np.dot(X, Y),sample_weight=W))
        if ii % 10 == 0:
            print('iteration %d is completed'%(ii))
    
    R_hat = np.dot(X, Y)
    print('Error of rated movies: %.5f'%(mean_squared_error(R, np.dot(X, Y), sample_weight=W)))
    return(R_hat, errors)
