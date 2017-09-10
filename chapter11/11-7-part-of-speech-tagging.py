from nltk.tag import StanfordPOSTagger
from nltk.tokenize import word_tokenize

STANFORD_POS_MODEL_PATH = '압축을 푼 장소/models/english-bidirectional-distsim.tagger'
STANFORD_POS_JAR_PATH = '압축을 푼 장소/stanford-postagger-3.6.0.jar'

pos_tagger = StanfordPOSTagger(STANFORD_POS_MODEL_PATH, STANFORD_POS_JAR_PATH)

# 임의로 만들어낸 예제입니다. 이 부분을 원하는 문장으로 바꿔서 실습하세요.
text = 'One day in November 2016, the two authors of this book, Seungyeon and Youngjoo, had a coffee at Red Rock cafe, which is a very popular place in Mountain View.'

tokens = word_tokenize(text)
print(tokens)  # 쪼개진 토큰을 출력합니다.
print()
print(pos_tagger.tag(tokens))  # 품사 태깅을 하고 그 결과를 출력합니다.

# 동사와 명사만 뽑아봅시다.
noun_and_verbs = []
for token in pos_tagger.tag(tokens):
    if token[1].startswith('V') or token[1].startswith('N'):
        noun_and_verbs.append(token[0])
print(', '.join(noun_and_verbs))
