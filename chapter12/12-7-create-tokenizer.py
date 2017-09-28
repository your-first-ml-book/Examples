from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer

class LemmaTokenizer(object):
    def __init__(self):
        self.tokenizer = RegexpTokenizer('(?u)\w\w+')
        # TfidfVectorizer와 같은 방식으로 키워드를 가져옵니다.
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return([self.wnl.lemmatize(t) for t in self.tokenizer.tokenize(doc)])
     
# 사이킷런에 위에서 정의한 토크나이저를 입력으로 넣습니다.
vectorizer2 =TfidfVectorizer(min_df=1,tokenizer=LemmaTokenizer(),stop_words='english')
X = vectorizer2.fit_transform(movie_plot_li)
feature_names = vectorizer2.get_feature_names()
