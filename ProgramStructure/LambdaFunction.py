'''
 pyhon中用关键字lambda来定义匿名函数
 <函数名> = lambda<参数列表>:表达式
'''

f = lambda x, y: x + y
print(f(10, 20))

# pow(x,n) x:参数 n:对先进性n次方
temp = lambda x: pow(x, 2)
print(temp(10))


ls = [['a',100],['b',10],['c',30],['d',90],['e',50]]
ls.sort(key=lambda x:x[1])
print(ls)