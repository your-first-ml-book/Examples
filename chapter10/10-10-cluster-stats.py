
def analyze_clusters_product_count(label, user_product_dic, id_user_dic):
    product_len_dic = {}
    for i in range(0, len(label)):
        product_len_dic.setdefault(label[i], [])
        # 클러스터의 ID를 키로 하는 딕셔너리에
        # 그 클러스터에 속한 사용자가 구매한 고유 상품의 가짓수를 저장합니다.
        product_len_dic[label[i]].append(len(user_product_dic[id_user_dic[i]]))
    for k, v in product_len_dic.items():
        print('cluster:', k)
        print(stats.describe(v))
        
analyze_clusters_product_count(km_plus.labels_, user_product_dic,id_user_dic)
