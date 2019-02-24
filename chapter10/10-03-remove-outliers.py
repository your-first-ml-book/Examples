# 구매한 상품의 가짓수가 1인 사용자의 사용자 ID를 찾습니다.
min_product_user_li =[k for k,v in user_product_dic.items() if len(v)==1]
# 마찬가지로, 구매한 상품의 가짓수가 600개 이상인 사용자의 사용자 ID를 찾습니다.
max_product_user_li =[k for k,v in user_product_dic.items() if len(v)>=600]
print("# of users purchased one product:%d" % (len(min_product_user_li)))
print("# of users purchased more than 600 product:%d" % (len(max_product_user_li)))
# 찾아낸 사용자를 군집화에 사용할 user_product_dic에서 제외합니다.
user_product_dic = {k:v for k,v in user_product_dic.items() if len(v)>1 and len(v)<600}
print("# of left user:%d" % (len(user_product_dic)))
# 남아 있는 사용자가 구매한 상품에도 0에서 시작하는 고유 ID를 부여합니다.
# 데이터셋에서 제외된 사용자가 구매한 상품은 군집화에서 사용하지 않기 때문에 이러한 처리를 해야 합니다.
id_product_dic = {}
for product_set_li in user_product_dic.values():
    for x in product_set_li:
        if x in id_product_dic:
            product_id = id_product_dic[x]
        else:
            id_product_dic.setdefault(x, len(id_product_dic))
print("# of left items:%d" % (len(id_product_dic)))
