from sklearn.cluster import KMeans
import random

# 학습용과 평가용 데이터로 나누기 위해 사용자-상품 벡터를 셔플합니다.
random.shuffle(user_product_vec_li)

# 학습용 데이터에 사용자 2500명을, 평가용 데이터에 나머지 사용자를 넣습니다.
# 학습용 데이터에 있는 사용자 정보만을 가지고 클러스터를 만든 후
# 평가용 데이터의 사용자가 어느 클러스터에 속하는지 알아봅니다.
train_data = user_product_vec_li[:2500]
test_data = user_product_vec_li[2500:]

print("# of train data:% d, # of test_data: %d" % (len(train_data),len(test_data)))
# 학습 데이터를 군집화하여 4개의 클러스터를 생성한 후 그 결과를 km_predict에 저장합니다.
km_predict = KMeans(n_clusters=4, init='k-means++', n_init=10, max_iter=20).fit(train_data)

# km_predict 의 predict 함수를 이용하여 평가 데이터가 전 단계에서 만든 4개의 클러스터 중 어느 곳에
# 속하는지 살펴봅니다.
km_predict_result = km_predict.predict(test_data)
print(km_predict_result)
