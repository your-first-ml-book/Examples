import requests
import json
from sklearn.feature_extraction.text import TfidfVectorizer
result_lines = []
movie_plot_li = []
movie_title_li = []

# 영화 ID 1부터 100까지의 영화를 가져옵니다.
# [예제 12-1]에서 생성해둔 무비렌즈 영화 정보 리스트 movie_info_li를 이용합니다.
for movie_info in movie_info_li[:100]:
    movie_url = movie_info[3]
  
    if movie_url == '':
        # 무비렌즈 데이터에 url이 없을 경우의 예외 처리. 타이틀과 플롯은 공백으로 설정합니다.
        print(movie_info)
        movie_title_li.append('')
        movie_plot_li.append('')

    else:
        response = requests.get(movie_url)
        imdb_id = response.url.split('/')[-2]
        # print(imdb_id)
        if imdb_id == 'www.imdb.com':
            print('no imdb id of: %s' % (movie_info[0]))
            # IMDB ID가 없을 경우의 예외 처리
            movie_title = ''
            movie_plot = ''
    
        else:
            try:
                movie_response = requests.get('http://www.omdbapi.com/?i=' + imdb_id + '&plot=full&r=json')
        
            except MissingSchema:
                # OMDB API의 예외 처리
                print('wrong URL: %s' % (movie_info[0]))
                movie_title = ''
                movie_plot = ''

            try:
                movie_title = json.loads(movie_response.text)['Title']
                movie_plot = json.loads(movie_response.text)['Plot']
                #print(movie_response.text)
            except KeyError:
                # API 결과의 예외 처리
                print('incomplete json: %s' % (movie_info[0])))
                movie_title = ''
                movie_plot = ''
        
    result_lines.append("%s\t%s\n" % (movie_title, movie_plot))
    movie_plot_li.append(movie_plot)
    movie_title_li.append(movie_title)
    
print('download complete: %d movie data downloaded'%(len(movie_title_li)))
# 3개 이하의 문서에서 나오는 단어는 TF-IDF 계산에서 제외합니다. 스톱워드는 'english'로 합니다.
vectorizer = TfidfVectorizer(min_df=3, stop_words='english')
X = vectorizer.fit_transform(movie_plot_li)

# TF-IDF로 변환한 키워드의 리스트
# X의 0번 열에 해당하는 키워드가 feature_names[0]의 키워드입니다.
feature_names = vectorizer.get_feature_names()

