# 第一章课后作业题
import nltk
from nltk.book import *

# 1.尝试使用 Python 解释器作为一个计算器，输入表达式，如 12/(4+1)
print(12 / (4 + 1))

# 2.26个字母可以组成 26 的 10 次方或者 26**10 个 10 字母长的字符串。也就是 1411 67095653376L (结尾处的 L 只是表示这是 Python 长数字格式 )。
# 100 个字母长度的字符串可能有多少个?
print(26 ** 10)
print(26 ** 100)  # 每个位置可以放26个字母中任意一个，所以共有26的100次方个

# 3.Python 乘法运算可应用于链表。当你输入 ['Monty', 'Python'] * 20 或者 3 * sent1 会发生什么?
print(['Monty', 'Python'] * 20)
print(3 * sent1)

# 4.复习 1.1 节关于语言计算的内容。在 text2 中有多少个词?有多少个不同的词?
print(len(text2))
print(len(set(text2)))

# 5.比较表格 1-1 中幽默和言情小说的词汇多样性得分，哪一个文体中词汇更丰富?
# 幽默：4.3  小说：浪漫 8.3

# 6.制作《理智与情感》中四个主角:Elinor，Marianne，Edward 和 Willoughby 的分布图。
# 在这部小说中关于男性和女性所扮演的不同角色，你能观察到什么?你能找出一对夫妻吗?
fd = FreqDist(text2)
fd.tabulate()
roles = ['Elinor', 'Marianne', 'Edward', 'Willoughby']

# 7.查找 text5 中的搭配
text5.collocations()

# 8.思考下面的 Python 表达式:len(set(text4))。说明这个表达式的用途。描述在执行此计算中涉及的两个步骤。
# 查询text4中的词汇个数  set(text4)会去重  len()会计算个数

