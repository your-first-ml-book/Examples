import sys
import time
import glob
import unicodedata
from konlpy.tag import Mecab
from gensim.models import Word2Vec


#parameters
WINDOW=5
EMBEDDING_SIZE=200
BATCH_SIZE = 10000
ITER = 10

def read_text(fin):
    # 전처리된 위키백과 파일을 읽어 들입니다.
    corpus_li = []
    mecab = Mecab(dicpath='/opt/local/lib/mecab/dic/mecab-ko-dic')
    for line in open(fin):
        # 깨지는 글자를 처리하기 위해 unicodedata.normalize 함수를 이용해 
        # NFKC로변환합니다.
        line = unicodedata.normalize('NFKC', line)
        try:
            # 첫 글자가 숫자로 시작하는 문장을 말뭉치에 추가합니다.
            _ = int(line[0])
            corpus_li.append(' '.join(mecab.nouns(line)) + '\n')

        except ValueError:
            # 첫 글자가 한글로 시작하는 문장을 말뭉치에 추가합니다.
            if ord(line[0]) >= ord('가') and ord(line[0]) <= ord('힇'):
                corpus_li.append(' '.join(mecab.nouns(line))+'\n')
            else:
                pass
    print('# of lines in corpus',len(corpus_li))
    return(corpus_li)


def train_word2vec(corpus_li, fout_model):
    # read_text에서 생성한 말뭉치를 이용해 word2vec을 학습시킵니다.
    model = Word2Vec(corpus_li, sg=1, size=EMBEDDING_SIZE, window=WINDOW, min_count=5, workers=3, batch_words=BATCH_SIZE, iter=ITER)
    model.init_sims(replace=True) #clean up memory
    model.save(fout_model)
    return(model)



# 전처리된 파일을 한번에 읽어 들이기 위한 정규식
input_pattern = '/Users/forumai/Downloads/kor_wiki/kowiki-latest-pages-articles.xml-88.txt'
fin_li = glob.glob(input_pattern)

for fin in fin_li:
    corpus_li = read_text(fin)

# 모델학습
model = train_word2vec(corpus_li, '/Users/forumai/Downloads/kor_wiki/test_model.txt')
print(model.most_similar('프랑스', topn=20))
print(model.most_similar(positive=['한국','파리'], negative=['서울']))



