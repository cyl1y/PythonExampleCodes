# 创建列表
list1 = [1, 2, 3]
list2 = list('python')
list3 = ['a', 'b', 'c']
tp = ('学号','专业','python')
list4 = list(tp)
print(list4)
list5 = ['学号', '专业', 'python', ['高等数学', '线性代数', '概率论']]
print(list5[3][0])

# 列表操作
"""将一个列表的值赋给另一个变量"""
ls = ['a','b','c','d','e',[1,2,3,4,5,6]]
ls2 = ls.copy()
print(ls2)

"""列表元素访问与操作"""
ls1 = ['cat','dog','tiger',123]
del ls1[3]
ls1.append('monkey')
ls1.insert(3,'+1')
print(ls1)
ls1.pop(3)
ls1.reverse()
print(ls1)

"""列表元素遍历"""
sum = 0
for i in ls1:
    sum +=1
print(sum)