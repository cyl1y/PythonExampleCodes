sample_str = "   Hello, World!   "

# 将字符串转换为小写
lowercase_str = sample_str.lower()
print(lowercase_str)

# 将字符串转换为大写
uppercase_str = sample_str.upper()
print(uppercase_str)

# 去掉左右两侧的空白字符
stripped_str = sample_str.strip(   )
print(stripped_str)

# 统计hello在字符串中出现的次数
countcase_str = sample_str.count('Hello')
print(countcase_str)

# 指定字符串World在字符串中的位置
find_str = sample_str.find('World')
print(find_str)
find_str1 = sample_str.find('x')
print(find_str1)
index_str = sample_str.index('World')
print(index_str)
# index_str1 = 'find'.index('x')
# print(index_str1)

# 替换字符串中Hello为Hlao
replace_str = sample_str.replace('Hello','Hlao')
print(replace_str)

# 用空字符将字符串分割
split_str = sample_str.split( )
print(split_str)

# 用-将split_str字符串重新组合
join_str = '-'.join(split_str)
print(join_str)

# 是以指定字串开始返回True,否则为False
starts_withhello1 = sample_str.startswith("Hello")
print(starts_withhello1)
starts_withhello2 = sample_str.startswith("Hello",3)
print(starts_withhello2)
starts_withhello3 = sample_str.startswith("Hello",3,4)
print(starts_withhello3)
starts_withhello4 = sample_str.startswith("Hello",3,8)
print(starts_withhello4)

# 以指定字符串结束则为True,否则为False
ends_withstr = sample_str.endswith("World")
print(ends_withstr)
ends_withstr1 = sample_str.endswith("   ")
print(ends_withstr1)

# 当字符串所有字符串为空格时，返回true，否则false
is_space = sample_str.isspace()
print(is_space)
is_space1 = '   '.isspace()
print(is_space1)

# 当字符串所有字符串为数字时，返回true，否则false
is_numeric = sample_str.isnumeric()
print(is_numeric)
is_numeric1 = '1234'.isnumeric()
print(is_numeric1)


# 当字符串所有字符串为数字时，返回true，否则false
is_printable = sample_str.isprintable()
print(is_printable)

# 当字符串所有字符串为小写时，返回true，否则false
is_lower = sample_str.islower()
print(is_lower)

# format()格式化
formatted_str = "My name is {},and I'm {} years old.".format("Alice",30)
print(formatted_str)

# 指定返回"hello"字符串的副本，长度为10
zifll_str = 'hello'.zfill(10)
print(zifll_str)

# 指定字符串'python'居中,总长度长度为20
center_str = 'python'.center(20,'*')
print(center_str)

