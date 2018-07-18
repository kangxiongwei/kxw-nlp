# NLP文本语料
import nltk
from nltk.corpus import gutenberg

# 古腾堡语料库
print(gutenberg.fileids())

emma = gutenberg.words('austen-emma.txt')
print(len(emma))

emma = nltk.Text(emma)
print(emma.concordance('surprize'))

for fileid in gutenberg.fileids():
    num_chars = len(gutenberg.raw(fileid))
    num_words = len(gutenberg.words(fileid))
    num_sents = len(gutenberg.sents(fileid))
    num_vocab = len(set(w.lower() for w in gutenberg.words(fileid)))
    # 打印平均词长、平均句子长度、每个词出现的平均次数
    print(int(num_chars / num_words), int(num_words / num_sents), int(num_words / num_vocab), fileid)

