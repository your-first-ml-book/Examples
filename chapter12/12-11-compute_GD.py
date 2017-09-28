def compute_GD(R,n_iter, lambda_, learning_rate, k):
    m,n =R.shape
    errors=[]
        
    X = np.random.rand(m, k)
    Y = np.random.rand(k, n)
    
    # 입력받은 반복 횟수만큼 갱신을 반복합니다.
    for ii in range(n_iter):
        for u in range(m):
            for i in range(n):
                if R[u,i]>0:
                    # 새로 정의된 갱신식. 각 사용자 및 상품의 행렬에 대해 하나씩 계산합니다.
                    e_ui = R[u,i]-np.dot(X[u, :], Y[:,i])

                    X[u,:] = X[u,:] + learning_rate * (e_ui* Y[:,i] - lambda_ * X[u,:])
                    Y[:,i] = Y[:,i] + learning_rate * (e_ui * X[u,:] - lambda_ * Y[:,i])  
                    
        errors.append(mean_squared_error(R, np.dot(X, Y)))
        
        if ii % 10 == 0:
            print('iteration %d is completed'%(ii))

    R_hat = np.dot(X, Y)
    print('Error of rated movies: %.5f'%(mean_squared_error(R, R_hat)))

    return(R_hat, errors)


