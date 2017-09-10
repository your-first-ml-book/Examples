from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize

STANFORD_NER_CLASSIFER_PATH = '압축을 푼 장소/classifiers/english.muc.7class.distsim.crf.ser.gz'
STANFORD_NER_JAR_PATH = '압축을 푼 장소/stanford-ner-3.6.0.jar'

ner_tagger = StanfordNERTagger(STANFORD_NER_CLASSIFER_PATH, STANFORD_NER_JAR_PATH)

# 임의로 만든 예제입니다. 이 부분을 원하는 문장으로 바꿔서 실습하세요.
text = 'One day in November 2016, the two authors of this book, Seungyeon and Youngjoo, had a coffee at Red Rock cafe, which is a very popular place in Mountain View.'

tokens = word_tokenize(text)
print(ner_tagger.tag(tokens))

# 장소에 해당하는 단어만 출력합니다.
all_locations = []
for token in ner_tagger.tag(tokens):
    if token[1] == 'LOCATION':
        all_locations.append(token[0])
print(', '.join(all_locations))
