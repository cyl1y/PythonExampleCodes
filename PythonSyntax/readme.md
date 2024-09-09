# Python 基本语法

### Python 的格式框架

在Python中，普遍采用的是PEP 8的编码规范，采用严格的缩进来表示代码块的开始和结束。

- 缩进：使用4个空格作为缩进单位，不允许使用制表符（tab）进行缩进。
- 行长度：每行代码的长度不应超过79个字符。
- 空行：在函数或类中，可以使用空行来组织代码，增强可读性。

### 注释

注释是代码中添加的说明性文字，用于解释代码的功能和作用。Python支持单行注释和多行注释。

- 单行注释：使用#符号表示，其后跟注释内容。
- 多行注释：使用三个单引号或三个双引号表示，可以跨越多行。

### 变量名和保留字

- 在Python中，变量名可以由字母、数字和下划线组成，但变量名不能以数字开头。
- Python中有一些保留字，不能用作变量名。
- 变量名对大小写敏感，如str和Str是两个不同的变量。
- python中的保留字：

| and        | as         | assert     | break       |
| --------- | ---------- | ----------- | ----------- |
| class      | continue    | def          | del          |
| elif       | else        | except      | exec         |
| finally    | for          | from         | global       |
| import    | in           | is           | lambda       |
| nonlocal   | not         | or           | pass         |
| raise      | return      | try          | while         |
| with        | yield        | ascii       | bytes        |
| exec_      | not_in      | round        | True         |
| False      | None        | ellipsis     | help         |
| __import__ | __builder__ | __loader__ | __name__     |
| __package__ | __spec__   | yield_from   |

### 赋值语句
赋值语句是Python中最基本的语句，用于将一个值赋给一个变量。在Python中，可以使用等号（=）来完成赋值操作。

```python
x = 5
y = "Hello"
z = True
```
##### 多个变量赋值
按照顺序将右侧表达式的值赋给左侧变量。

```python
x, y, z = 5, "Hello", True
```
##### 交换赋值
将两个变量的值互换。

```python
x, y = y, x
```
##### 增量赋值

```python
x = 5
x += 3  # 等同于 x = x + 3
y = 10
y *= 5  # 等同于 y = y * 5
```
##### 多重赋值
同时将多个值赋给多个变量。

```python
a = b = c = 10
```
使用多个变量接收一个可迭代对象的值

```python
x, y, z = (1, 2, 3)
```

###  常用函数

#### 类型转换

#####  int():将其他类型转换为整数类型

```python
num_float = 3.14
num_int = int(num_float)
print(num_int)  # 输出: 3
```

```python
num_str = "123"
num_int = int(num_str)
print(num_int)  # 输出: 123   
```
##### float():将其他类型转换为浮点数类型

```python
num_int = 123
num_float = float(num_int)
print(num_float)  # 输出: 123.0
```

```python
num_str = "3.14"
num_float = float(num_str)
print(num_float)  # 输出: 3.14
```

##### str():将其他类型转换为字符串类型

```python
num_int = 123
num_str = str(num_int)
print(num_str)  # 输出: "123"
```

```python
num_float = 3.14
num_str = str(num_float)
print(num_str)  # 输出: "3.14"
```

##### bool():将其他类型转换为布尔类型

```python
num_int = 0
num_bool = bool(num_int)
print(num_bool)  # 输出: False
```

```python
num_int = 1
num_bool = bool(num_int)
print(num_bool)  # 输出: True
```

##### list(),tuple(),set():将其他可迭代对象转换为列表、元组、集合

```python
str_list = list("Hello")
print(str_list)  # 输出: ['H', 'e', 'l', 'l', 'o']
```

```python
num_list = [1, 2, 3]
num_tuple = tuple(num_list)
print(num_tuple)  # 输出: (1, 2, 3)
```

```python
num_list = [1, 2, 3]
num_set = set(num_list)
print(num_set)  # 输出: {1, 2, 3}
```


```python
num_tuple = (1, 2, 3)
num_list = list(num_tuple)
print(num_list)  # 输出: [1, 2, 3]
```

```python
num_set = {1, 2, 3}
num_list = list(num_set)
print(num_list)  # 输出: [1, 2, 3]
```

##### dict():将其他类型转换为字典

```python
num_dict = dict(a=1, b=2, c=3)
print(num_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}
```

```python
num_dict = dict([('a', 1), ('b', 2), ('c', 3)])
print(num_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}
```

```python
num_dict = dict({'a': 1, 'b': 2, 'c': 3})
print(num_dict)  # 输出: {'a': 1, 'b': 2, 'c': 3}
```

#### 数学函数

##### abs():求绝对值

```python
num_abs = abs(-5)
print(num_abs)  # 输出: 5
```

##### round():四舍五入

```python
num_round = round(3.14159, 2)
print(num_round)  # 输出: 3.14
```

##### pow():幂运算

```python
num_pow = pow(2, 3)
print(num_pow)  # 输出: 8
```

##### max():求最大值

```python
num_max = max(1, 2, 3, 4, 5)
print(num_max)  # 输出: 5
```

##### min():求最小值

```python
num_min = min(1, 2, 3, 4, 5)
print(num_min)  # 输出: 1
```

##### sum():求和

```python
num_sum = sum([1, 2, 3, 4, 5])
print(num_sum)  # 输出: 15
```

#### 序列操作函数

##### len():求长度
len()可以返回序列长度（求元素个数），也可以返回字符串长度

```python
num_len = len([1, 2, 3, 4, 5])
print(num_len)  # 输出: 5
```

##### sorted():排序

```python
num_sorted = sorted([3, 1, 2, 5, 4])
print(num_sorted)  # 输出: [1, 2, 3, 4, 5]
```

##### reversed():反转

```python
num_reversed = reversed([1, 2, 3, 4, 5])    
print(list(num_reversed))  # 输出: [5, 4, 3, 2, 1]
```

#### 字符串处理函数

##### capitalize():首字母大写

```python
str_capitalize = "hello world".capitalize()
print(str_capitalize)  # 输出: Hello world
```

#####title():每个单词首字母大写

```python
str_title = "hello world".title()
print(str_title)  # 输出: Hello World
```

##### upper():全部大写

```python
str_upper = "hello world".upper()
print(str_upper)  # 输出: HELLO WORLD
```

#####lower():全部小写

```python
str_lower = "Hello World".lower()
print(str_lower)  # 输出: hello world
```

##### split():将字符串按指定字符分割

```python
str_split = "hello,world".split(",")
print(str_split)  # 输出: ['hello', 'world']
```

##### count():统计某个字符或字符串出现的次数

```python
str_count = "hello world".count("o")
print(str_count)  # 输出: 2
```

##### swapcase():大小写互换

```python
str_swapcase = "Hello World".swapcase()
print(str_swapcase)  # 输出: hELLO wORLD
```

##### replace():替换字符串

```python
str_replace = "hello world".replace("world", "python")
print(str_replace)  # 输出: hello python
```

##### center():居中显示

```python
str_center = "hello".center(10)
print(str_center)  # 输出:   hello
```

#### 其他

##### type():获取变量的类型

```python
num_type = type(123)
print(num_type)  # 输出: <class 'int'>
```

##### range():生成一个整数序列

```python
range_num = range(1, 10)
print(list(range_num))  # 输出: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

##### eval():将字符串转换为Python表达式或数值

```python
eval_num = eval("1+2")
print(eval_num)  # 输出: 3
```