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
# 将一个列表的值赋给另一个变量
ls = ['a','b','c','d','e',[1,2,3,4,5,6]]
ls2 = ls.copy()
print(ls2)

# 列表元素访问与操作
ls1 = ['cat','dog','tiger',123]
del ls1[3]
ls1.append('monkey')
ls1.insert(3,'+1')
print(ls1)
ls1.pop(3)
ls1.reverse()
print(ls1)

# 列表元素遍历
sum = 0
for i in ls1:
    sum +=1
print(sum)

# 对列表元素求平均值
ls_r = [20,10,7,6,31]
sum = 0
for i in ls_r:
    sum += i
print("平均值：",sum/len(ls_r))

# 删除3的倍数
ls_d = [23,45,78,87,11,67,89,13,243,56,67,311,431,111,141]
lt = ls_d.copy()
count = 0
print('ls_d=',end=' ')
for i in ls_d:
    if i % 3 == 0:
        lt.remove(i)
        count += 1
    else:
        print(i,end=' ')
print('\n总删除{}个元素'.format(count))

# 创建集合
s_1 = {1,2,3,4,5}
s_2 = set('python')
s_3 = set(('python',123))
print(s_1)
print(s_2)
print(s_3)