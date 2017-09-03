import sys
import time
import glob
import unicodedata
from konlpy.tag import Mecab
from gensim.models import Word2Vec

hangul_start = 44032 #가
hangul_end = 55203 #힣

#parameters
WINDOW=5
EMBEDDING_SIZE=200
BATCH_SIZE = 10000
ITER = 10

def read_text(fin):
    corpus_li = []
    mecab = Mecab(dicpath='/opt/local/lib/mecab/dic/mecab-ko-dic')
    for line in open(fin):
        line = unicodedata.normalize('NFKC', line)
        try:
            _ = int(line[0])
            corpus_li.append(' '.join(mecab.nouns(line)) + '\n')

            # pos_li = ['%s\t%s\n' % (v[0], v[1]) for v in mecab.pos(line)]
            # result_lines.extend(pos_li)
        except ValueError:
            if ord(line[0]) >= hangul_start and ord(line[0]) <= hangul_end:
                # result_lines.append(line)
                corpus_li.append(' '.join(mecab.nouns(line))+'\n')
                # pos_li = ['%s\t%s\n' % (v[0], v[1]) for v in mecab.pos(line)]
                # result_lines.extend(pos_li)

            else:
                pass

    return(corpus_li)


def train_word2vec(corpus_li, fout_model):

    model = Word2Vec(corpus_li, sg=1, size=EMBEDDING_SIZE, window=WINDOW, min_count=5, workers=3, batch_words=BATCH_SIZE, iter=ITER)
    model.init_sims(replace=True) #clean up memory
    model.save(fout_model)
    return(model)




if __name__ == '__main__':

    argv = sys.argv

    input_pattern = '/Users/forumai/Downloads/kor_wiki/kowiki-latest-pages-articles.xml-88.txt'
    fin_li = glob.glob(input_pattern)

    for fin in fin_li:
        corpus_li = read_text(fin)
        model = train_word2vec(corpus_li, '/Users/forumai/Downloads/kor_wiki/test_model.txt')
        print(model.most_similar('프랑스', topn=20))
        print(model.most_similar(positive=['한국','파리'], negative=['서울']))



