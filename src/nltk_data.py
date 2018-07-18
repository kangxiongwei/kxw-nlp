from __future__ import division
import nltk
from nltk.book import *

# 查询关键字对应的上下文
print('--------------------------')
text1.concordance('monstrous')

# 查询关键字对应的上下文，查找具有相似上下文的单词
print('--------------------------')
text1.similar("monstrous")

# 查询两个及两个以上词共同的上下文
print('--------------------------')
text2.common_contexts(['monstrous', 'very'])

# 离散图表示单词在文中出现的位置
# print('--------------------------')
# text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

# 产生一些随机文本，重用了文中常见的词和短语，从而感觉文章的风格和内容
print('--------------------------')
text3.generate('monstrous')

# 获取文本长度
print('--------------------------')
print(len(text3))

print(sorted(set(text3)))
print(len(set(text3)))

print(len(text3) / len(set(text3)))

print(text3.count('smote'))

# text5 中 lol 出现了多少次?它占文本全部词数的百分比是多少?
print("int text5 lol appeared %d times" % (text5.count('lol')))
print("int text5 lol ratio is %f " % (100 * text5.count('lol') / len(text5)))

# 链表
print('--------------------------')
sent1 = ['Call', 'me', 'Ishmael', '.']
print(sent1)
print(len(sent1))

sent2 = ['The', 'family', 'of', 'Dashwood', 'had', 'long', 'been', 'settled', 'in', 'Sussex', '.']

sent3 = sent1 + sent2
print(sent3)

# 追加元素
sent3.append('new')

# 链表索引
print('--------------------------')
print(text4[173])  # 查找第173个位置的单词
print(text4.index('awaken'))  # 查询单词对应的索引位置

# 链表切片
print(text5[1:10])

# 字符串
print('--------------------------')
name = 'Monty'
print(name[0])  # M 索引字符串
print(name[:4])  # Mont 切片字符串
print(name * 2)  # MontyMonty 乘法
print(name + '!')  # Monty! 加法
print(' '.join(['Monty', 'Python']))  # 链表转成字符串，用' '间隔
print('Monty Python'.split())  # 字符串转成链表

# 频率分布
print('--------------------------')
fdist1 = FreqDist(text1)  # 统计词汇频率
print(fdist1)

vocabulary1 = list(fdist1.keys())  # 文中出现的所有词汇
print(vocabulary1[:50])  # 出现次数前50的词汇
print(fdist1['whale'])  # whale的出现次数
print(fdist1.hapaxes())  # 只出现了一次的词
fdist1.plot(50, cumulative=True)  # 书中50个词的累积频率图

# 高频和低频词汇，对句子没有意义时，可以考虑其他词，下面挑选单词长度大于15的词
print('--------------------------')
V = set(text1)
long_words = [w for w in V if len(w) > 15]  # 挑出长度大于15的单词
print(sorted(long_words))
dist1 = sorted([w for w in set(text1) if len(w) > 7 and fdist1[w] > 7])  # 挑选长度大于7且出现次数大于7的单词分析
print(dist1)

# 词汇搭配和双连词
print('--------------------------')
print(bigrams(['more', 'is', 'said', 'than', 'done']))  # 双连词
print(text4.collocations())  # 文中出现频率最高的连词

# 统计词长的频率分布
print('--------------------------')
fdist = FreqDist([len(w) for w in text1])
print(fdist)
print(list(fdist.keys()))
print(fdist.items())  # 每个词长对应的频次
print(fdist.max())  # 出现次数最多的词长
print(fdist[3])  # 3个字符的单词出现多少次
print(fdist.freq(3))  # 3个字符的单词占比是多少

# 嵌套代码块
print('--------------------------')
word = 'cat'
# if语句，缩进4个空格
if len(word) < 5:
    print("word is less than 5")
# for循环，缩进4个空格
for word in sent1:
    print(word)
# 结合使用
for word in sent1:
    if len(word) > 5:
        print("word is more than 5")
    elif len(word) <= 5:
        print('word is less than 5')

# 机器翻译
# NLTK3不再支持
