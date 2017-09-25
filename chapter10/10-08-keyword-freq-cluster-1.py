def analyze_clusters_keywords(labels,product_id_name_dic,user_product_dic, id_user_dic):
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
        
        # 각 클러스터안의 상품명을 join명령으로 합쳐 하나의 문자열로 만든 뒤
        # 스페이스 혹은 탭으로 스플릿하여 키워드로 분해합니다. 
        product_name_keyword = (" ").join(product_name).split()

        # 클러스터의 아이디와, 그 아이디를 가지는 클러스터에 속하는 유저들이 구매한 상품들의 상품명안에
        # 가장 자주 나타나는 단어 20개를 역순으로 출력합니다
        print("cluster_id:", cluster_id)
        print(Counter(product_name_keyword).most_common(20))
        
km=KMeans(n_clusters=2, n_init=10,max_iter=20)
km.fit(test_data)
analyze_clusters_keywords(km.labels_,product_id_name_dic,user_product_dic,id_user_dic)
