import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

spam_header = 'spam\t'
no_spam_header = 'ham\t'
documents = []
labels = []

with open('SMSSpamCollection') as file_handle:
    for line in file_handle:
        # 각 줄에서 레이블 부분만 떼어내고 나머지를 documents에 넣습니다.
        if line.startswith(spam_header):
            labels.append(1)
            documents.append(line[len(spam_header):])
        elif line.startswith(no_spam_header):
            labels.append(0)
            documents.append(line[len(no_spam_header):])

vectorizer = CountVectorizer()  # 단어 횟수 피처를 만드는 클래스입니다.
term_counts = vectorizer.fit_transform(documents)  # 문서에서 단어 횟수를 셉니다.
vocabulary = vectorizer.get_feature_names()

# 단어 횟수 피처에서 단어 빈도 피처를 만드는 클래스입니다.
# tf-idf에서 idf를 생성하지 않으면 단어 빈도(term frequency)가 만들어집니다.
tf_transformer = TfidfTransformer(use_idf=False).fit(term_counts)
features = tf_transformer.transform(term_counts)

# 처리된 파일을 저장합니다. 앞으로의 예제에서 사용될 예정입니다.
with open('processed.pickle', 'wb') as file_handle:
    pickle.dump((vocabulary, features, labels), file_handle)
