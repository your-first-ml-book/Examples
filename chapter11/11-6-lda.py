from sklearn.decomposition import LatentDirichletAllocation
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

spam_header = 'spam\t'
no_spam_header = 'ham\t'
documents = []

# 위와는 다르게 레이블을 만들 필요는 없습니다. 단순히 문서만을 추출합니다.
with open('SMSSpamCollection') as file_handle:
    for line in file_handle:
        if line.startswith(spam_header):
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            documents.append(line[len(no_spam_header):])

# LDA는 단어 빈도 피쳐가 아닌 단어가 나온 갯수가 잘 동작하기 때문에
# CountVectorizer를 사용합니다. 또한 토픽 모델에 도움이 되지 않는
# 단어들(stop_words)을 자동으로 제거합니다.
vectorizer = CountVectorizer(stop_words='english', max_features=2000)
term_counts = vectorizer.fit_transform(documents)
vocabulary = vectorizer.get_feature_names()

# 토픽 모델을 학습합니다.
topic_model = LatentDirichletAllocation(n_topics=10)
topic_model.fit(term_counts)

# 학습된 토픽들을 하나씩 출력합니다.
topics = topic_model.components_
for topic_id, weights in enumerate(topics):
    print('topic %d' % topic_id, end=': ')
    pairs = []
    for term_id, value in enumerate(weights):
        pairs.append( (abs(value), vocabulary[term_id]) )
    pairs.sort(key=lambda x: x[0], reverse=True)
    for pair in pairs[:10]:
        print(pair[1], end=',')
    print()
