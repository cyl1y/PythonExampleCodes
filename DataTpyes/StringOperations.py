sample_str = "   Hello, World!   "

# 将字符串转换为小写
lowercase_str = sample_str.lower()
#    hello, world!____
print(lowercase_str)

# 将字符串转换为大写
uppercase_str = sample_str.upper()
#    HELLO, WORLD!____
print(uppercase_str)

# 去掉左右两侧的空白字符
stripped_str = sample_str.strip(   )
# Hello, World!
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
#    Hlao, World!
print(replace_str)

# 用空字符将字符串分割
split_str = sample_str.split( )
# ['Hello,', 'World!']
print(split_str)

# 用-将split_str字符串重新组合
join_str = '-'.join(split_str)
# Hello,-World!
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
# True
print(is_space)
is_space1 = '   '.isspace()
# False
print(is_space1)

# 当字符串所有字符串为数字时，返回true，否则false
is_numeric = sample_str.isnumeric()
# True
print(is_numeric)
is_numeric1 = '1234'.isnumeric()
# True
print(is_numeric1)


# 当字符串所有字符串为数字时，返回true，否则false
is_printable = sample_str.isprintable()
# False
print(is_printable)

# 当字符串所有字符串为小写时，返回true，否则false
is_lower = sample_str.islower()
print(is_lower)

# format()格式化
formatted_str = "My name is {},and I'm {} years old.".format("Alice",30)
# My name is Alice,and I'm 30 years old.
print(formatted_str)

# 指定返回"hello"字符串的副本，长度为10
zifll_str = 'hello'.zfill(10)
# 00000hello
print(zifll_str)

# 指定字符串'python'居中,总长度长度为20
center_str = 'python'.center(20,'*')
# *******python*******
print(center_str)

# 字符串的格式化
# 1234+1234
print('%d+%d' % (1234,1234))
# +1234+1234
print('%+d%+d' % (1234,1234))
# -1234-1234
print('%+d%+d' % (-1234,-1234))
#   12,  1234,  3.140000
print('%4d,%6d,%10f' % (12,1234,3.14))
# 0012,001234,3.1400000000
print('%04d,%06d,%.10f' % (12,1234,3.14))
# 12  ,1234  ,3.140000__
print('%-4d,%-6d,%-10f' % (12,1234,3.14))
# 00000000000000000000000000000000000000000000000000000000000000000000000000000012,001234,3.1400000000
print('%080d,%06d,%.10f' % (12,1234,3.14))
# 12                                                                              ,1234  ,3.1400000000
print('%-80d,%-06d,%.10f' % (12,1234,3.14))

# 字符串和整数用法
name = 'pp'
age = 22
# my name is pp,my age is 22
print("my name is %s,my age is %d" % (name,age))
# my name is qq,my age is 20
print("my name is %(name)s,my age is %(age)d" % {'name':'qq','age':20})

# 默认浮点数精度是6
# 3.140000
print('%f' % 3.14)
# 3.1400
print('%.4f' % 3.14)


# format用法

#填充、对齐、宽度
str_value = 'HELLO'
# 0是参数序号，可忽略，30是宽度，实际位数小于指定宽度，位数将被默认以空格字符串补充，默认左对齐
# HELLO                         end
print('{0:30}end'.format(str_value))
# > 表示右对齐
#                          HELLOend
print('{0:>30}end'.format(str_value))
# 填充
# *^表示居中且用*填充,*也可以被其他替换
# ************HELLO*************end
print('{0:*^30}end'.format(str_value))
# 参数长度比<宽度>设定值大，使用参数实际长度
# HELLOend
print('{0}end'.format(str_value))

# 精度
# 浮点数
f_value = 123.4567
# 指定精度
print('{:.2f}'.format(f_value))
# 30为总位数，>右对齐，左边用*填充，输出：************************123.46
print("{:*>30.2f}".format(f_value))
# 字符串 输出：HEL
print('{}'.format(str_value[:3]))

# 号顺序
# 槽中无序号，按照出现的顺序进行替换；槽中有序号，按照序号顺序替换
day = '2023-01-12'
hours = 1
dis = 9.85
# 修改代码
# 2023-01-12,跑步1h,形成9.85km
print('{},跑步{}h,形成{}km'.format(day,hours,dis))
print('{2},跑步{0}h,形成{1}km'.format(hours,dis,day))

# 基本语法
# f-string
name = 'Alice'
age = 30
formatted_str = f"my name is {name} and my age is {age} years old."
# formatted_str = f"my name is {name} and my age is {age} years old."
print(formatted_str)

# 控制数字的小数字位数
pi = 3.1423471289047
formatted_pi = f"The value of pi is approximately {pi:.2f}"
# The value of pi is approximately 3.14
print(formatted_pi)

# 格式控制标记
# 整数类型(d)   Age:30
print("Age:{:d}".format(age))
print(f"Age:{age:d}")
# 浮点数类型(f)  Height:3.14
print("Height:{:.2f}".format(pi))
print(f"Height:{pi:.2f}")
# 字符串类型(s)  Name:Alice
print("Name:{:s}".format(name))
print(f"Name:{name:s}")
# 十六进制类型    Hex:ff
number = 255
print("Hex:{:x}".format(number))
print(f"Hex:{number:x}")
# 对齐和宽度
# <:左对齐    >:右对齐    ^:居中
# width:指定宽度
formatted_string = "{:*<10}{:->10}".format("left","right")
# left******-----right
print(formatted_string)
left = 'Left'
right = 'Right'
# left******-----right
print(f"{left:*<10}{right:->10}")
# ********Left********+++++++Right++++++++
print(f"{left:*^20}{right:+^20}")

# 验证那些数据类型可以作为dict的键
# 经过验证list\set\dict,包括其他可变的数据类型都不可以作为字典的键
dict1 = {'k1':[1,2,3,4],'k2':('a','b'),'k3':{12,13,14},'k4':{'k41':'a','k42':2}}
print(dict1)
dict2 = {('a','b'):'k1'}
print(dict2)