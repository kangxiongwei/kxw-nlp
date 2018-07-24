# 利用Jieba进行中文分词

import jieba

sent = "中文分词是文本处理不可或缺的一步！"

seg_list = jieba.cut(sent, cut_all=False)
print("精确模式:", "/ ".join(seg_list))

seg_list = jieba.cut(sent, cut_all=True)
print("全模式：", "/ ".join(seg_list))

seg_list = jieba.cut_for_search(sent)
print("搜索模式：", "/ ".join(seg_list))

