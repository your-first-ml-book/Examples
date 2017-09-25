# 예제 10-13
from sklearn.cluster import AgglomerativeClustering
ward = AgglomerativeClustering(n_clusters=2, affinity='euclidean',linkage='ward')
ward.fit(test_data)

# 예제 10-14
analyze_clusters_keywords_bigram(ward.labels_,product_id_name_dic,user_product_dic,id_user_dic)
