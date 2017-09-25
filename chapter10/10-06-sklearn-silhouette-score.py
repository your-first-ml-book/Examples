import numpy as np

from sklearn.metrics import silhouette_score
test_data = np.array(user_product_vec_li)

for k in range(2,9):
    km = KMeans(n_clusters=k).fit(test_data)
    print("score for %d clusters:%.3f" % (k, silhouette_score(test_data,km.labels_)))
