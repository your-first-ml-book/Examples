# 사용자 ID 참조를 위한 딕셔너리
id_user_dic = {}

# 군집화의 입력으로 사용할 리스트
user_product_vec_li = []

# 군집화에서 사용할 총 고유 상품 가짓수. 즉, 원-핫 인코딩으로 변환할 피처의 가짓수
all_product_count = len(id_product_dic)

for user_code, product_per_user_set in user_product_dic.items():
    # 고유 상품 가짓수를 길이로 하는 리스트 생성
    user_product_vec = [0] * all_product_count
    # id_user_dic의 길이를 이용하여 사용자 ID를 0부터 시작하는 user_id로 바꿉니다.
    id_user_dic[len(id_user_dic)] = user_code
    
    # 사용자가 구매한 상품 코드를 키로 하여 user_product_vec에서의
    # 해당 상품 코드의 상품 ID를 찾습니다. 그리고 값을 1로 세팅합니다.
    for product_name in product_per_user_set:
        user_product_vec[id_product_dic[product_name]] = 1
    
    # 한 사용자의 처리가 끝났으므로 이 사용자의 user_product_vec을 배열에 추가합니다.
    # 이때 배열의 인덱스는 새로 정의한 user_id가 됩니다.
    user_product_vec_li.append(user_product_vec)
