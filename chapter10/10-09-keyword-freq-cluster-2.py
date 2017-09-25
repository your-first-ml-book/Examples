def analyze_clusters_keywords_bigram(labels,product_id_name_dic,user_product_dic, id_user_dic):
    #각 클러스터의 아이디와, 해당 아이디의 클러스터 들어있는 유저 수를 출력합니다. 
    print(Counter(labels))
    cluster_item = {}

    for i in range(len(labels)):
        cluster_item.setdefault(labels[i], [])

        # 각 사용자의 임시 ID i에 대해 사용자 코드를 찾은 후
        # 그 사용자 코드와 연결된 구매상품의 ID를 참조한 후
        # 그 ID를 이용해 상품명을 찾아
        # 딕셔너리에 클러스터 ID를 키로, 상품명을 값으로 추가합니다.
        for x in user_product_dic[id_user_dic[i]]:
            cluster_item[labels[i]].extend([product_id_name_dic[x]])

    for cluster_id, product_name in cluster_item.items():
        # 각 클러스터 안의 상품명을 join 명령으로 합쳐 하나의 문자열로 만든 뒤
        # OF를 공백으로 리플레이스하고
        # 스페이스 혹은 탭으로 스플릿하여 키워드로 분해한 뒤
        # 연속되는 두 키워드를 합쳐서 하나의 키워드를 만듭니다.
        bigram = []
        product_name_keyword = (' ').join(product_name).replace(' OF ', ' ').split()
        for i in range(0, len(product_name_keyword) - 1):
            bigram.append(' '.join(product_name_keyword[i:i + 2]))
        print('cluster_id:', cluster_id)
        print(Counter(bigram).most_common(20))
        
km=KMeans(n_clusters=2, n_init=10,max_iter=20)
km.fit(user_product_vec_li)
analyze_clusters_keywords_bigram(km.labels_,product_id_name_dic,user_product_dic,id_user_dic)
