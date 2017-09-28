# 근사 행렬의 가장 작은 값을 0으로 만들고자 전체 항의 값에서 작은 값을 뺍니다.
R_hat -= np.min(R_hat)

# 근사 행렬의 가장 큰 값을 5로 만들고자 5를 가장 큰 예측값(np.max(R_hat))으로 나눈 값을 곱합니다.
# 예를 들어 가장 큰 예측값이 3일 경우 3을 5로 만들기 위해서는 5/3을 곱하면 됩니다.
# 위에서 구한 값을 예측 행렬의 모든 항에 곱합니다.
R_hat *= float(5) / np.max(R_hat)

def recommend_by_user(user):
    # 사용자의 ID를 입력으로 받아 그 사용자가 보지 않은 영화를 추천합니다.
    user_index = user-1
    user_seen_movies = sorted(list(enumerate(R_hat[user_index])),
    key=lambda x:x[1], reverse=True)
    recommended=1
    print("-----recommendation for user %d------"%(user))
    for movie_info in user_seen_movies:
        if W[u][movie_info[0]]==0:
            movie_title= movie_info_dic[str(movie_info[0]+1)]
            movie_score= movie_info[1]
            print("rank %d recommendation:%s(%.3f)"%(recommended,movie_title[0], movie_score))
        recommended+=1
        if recommended==6:
            break
