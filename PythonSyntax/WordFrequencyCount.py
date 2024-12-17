# 统计hamlet.txt
def get_text():
    # 获取文本，open(文件名，打开方式)，读取全文：read()
    file = open('hamlet.txt', 'r')
    text = file.read()
    # 统一大小写，统一转换为小写
    text = text.lower()
    # 去掉标点符号，标点符号不参与计数，用replace替换为空格
    for char in '!"#$%^&*()_+,/.?:";<>@[\\\\]''{|}':
        text = text.replace(char, '')
    return text


txt = get_text()
words = txt.split()
# 初始化一个空字典counts，用于存储每个单词及其出现的次数。
counts = {}
# 遍历文本
for w in words:
    # 用字字典的“d.get(key,default)+1"方法获取单词w的当前计数，如果单词不存在则默认为0，然后对这个计数加1。
    counts[w] = counts.get(w,0) + 1
# 将counts字典转换为一个列表，列表中的每个元素都是一个(key, value)对，并赋值给变量items
items = list(counts.items())
# 对items列表进行排序，排序依据是每个元素的第二项（即单词出现的次数），并设置reverse=True以便按降序排序
items .sort(key = lambda  x:x[1],reverse=True)
for i in range(10):
    # 使用for循环遍历前10个元素。
    word,counts = items[i]
    # 从排序后的列表中提取单词和对应的计数。
    print("{:<12}{:>5}".format(word,counts))
    # 打印单词和它的计数，使用格式化字符串来对齐输出，其中"<12"表示左对齐且宽度为12，">5"表示右对齐且宽度为5。
