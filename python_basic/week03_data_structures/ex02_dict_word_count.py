r"""
目标： 理解 dict 的键值结构、计数用法。
要求：
定义一个字符串，例如：
text = "hello world hello python hello code"
按空格切分成单词列表。
用 dict 统计每个单词出现次数，得到类似：
{"hello": 3, "world": 1, "python": 1, "code": 1}
打印这个 dict，并找出出现次数最多的单词。
提示：
可以用 if word in counts: 这种写法；
也可以练习 dict.get(word, 0)。"""


if __name__ == "__main__":
    text = "hello world hello python hello code"
    words = text.split(" ")
    print(words)
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
            print(counts)
        else:
            counts[word] = 1
            print(counts)
    print(counts)
    # 使用dict.get(word, 0)来统计
    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1
    print(counts)
    # 找出出现次数最多的单词
    max_count = 0
    max_word = ""
    for word, count in counts.items():
        if count > max_count:
            max_count = count
            max_word = word
    print(max_word)

    



