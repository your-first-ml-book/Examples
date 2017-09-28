# 예제 12-12 
def train_test_split(R, n_test):
    train = R.copy()
    # 모든 항이 0으로 채워진 학습용 별점 행렬을 만듭니다.
    test = np.zeros(R.shape)
    
    for user in range(R.shape[0]):
        # 각 시용자마다 n_test개의 0이 아닌 항(사용자가 입력한 별점)을 임의로 골라
        # 인덱스를 기억합니다.
        test_index = np.random.choice(R[user, :].nonzero()[0], size=n_test,replace=False)
        
        # 위에서 정한 인덱스에 해당하는 별점을 0으로 만듭니다.
        train[user, test_index] = 0
        
        # 평가 데이터 행렬의 해당 인덱스에 사용자가 입력한 실제 별점을 입력합니다.
        test[user, test_index] = R[user, test_index]
    return(train, test)

# 예제 12-13
def get_test_mse(true,pred):
    # 학습-평가 데이터에서 0이 아닌 값만 이용해서 에러를 계산합니다.
    # true가 평가 데이터, pred가 학습 데이터입니다.
    # 평가 데이터가 0이 아닌 항들의 인덱스에 해당하는 점수만 추출합니다.
    pred = pred[true.nonzero()].flatten()
    true = true[true.nonzero()].flatten()
    return mean_squared_error(true,pred)
