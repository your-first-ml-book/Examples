from sklearn.metrics.pairwise import cosine_similarity

movie_sim = cosine_similarity(X)
def similar_recommend_by_movie_id(movielens_id):
  movie_index = movielens_id-1
  # enumerate 함수로 [(리스트 인덱스 0, 유사도 0), (리스트 인덱스 1, 유사도 1)...]의
  # 리스트를 만듭니다. 그 후 각 튜플의 두 번째 항목, 즉 유사도를 이용하여 내림차순 정렬합니다.
  # 이렇게 만든 리스트의 가장 앞 튜플의 첫 번째 항목이 영화 ID가 됩니다.
  similar_movies = sorted(list(enumerate(movie_sim[movie_index])),key=lambda x:x[1], reverse=True)
  recommended=1
  print("-----recommendation for movie %d------"%(movie))
  for movie_info in similar_movies[1:7]:
    # 주어진 영화와 가장 비슷한 영화는 그 영화 자신이므로 출력 시 제외합니다.
    movie_title= movie_info_li[movie_info[0]]
    print('rank %d recommendation:%s'%(recommended,movie_title[0]))
    recommended+=1
