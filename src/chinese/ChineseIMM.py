# 中文分词技术


class IMM(object):

    def __init__(self, dic_path):
        self.dictionary = set()
        self.maximum = 0
        # 读取词典
        with open(dic_path, 'r', encoding='utf8') as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                self.dictionary.add(line)
                self.maximum = max(self.maximum, len(line))

    # 反向最大匹配法
    def reversed(self, text):
        result = []
        # 输入的文本长度
        index = len(text)
        while index > 0:
            word = None
            # size可以取值1，2，3，4
            for size in range(self.maximum, 0, -1):
                if index - size < 0:
                    continue
                piece = text[(index - size):index]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index -= size
                    break
            if word is None:
                index -= 1
        # 将结果逆序输出
        return result[::-1]

    # 正向最大匹配法
    def forward(self, text):
        result = []
        index = 0
        length = len(text)
        while index < length:
            word = None
            # 词长 4 3 2 1
            for size in range(self.maximum, 0, -1):
                if index + size > length:
                    continue
                piece = text[index:(index + size)]
                if piece in self.dictionary:
                    word = piece
                    result.append(word)
                    index += size
                    break
            if word is None:
                index += 1
        # 返回结果
        return result

    # 双向最大匹配算法
    def both(self, text):
        rev = self.reversed(text)
        fw = self.forward(text)
        len1 = len(rev)
        len2 = len(fw)
        return fw if len1 > len2 else rev


def main():
    text = "南京市长江大桥"
    tokenizer = IMM('./data/imm_dic.utf8')
    print(tokenizer.reversed(text))
    print(tokenizer.forward(text))
    print(tokenizer.both(text))


main()
