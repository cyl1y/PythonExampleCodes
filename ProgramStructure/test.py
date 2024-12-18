
# for -else
# else之后的语句块只有在循环正常结束才能执行
for c in 'abc':
    print('循环进行中:'+c)
else:
    print('循环结束！')

# while循环
sum = 0
i = 0
while i <= 100:
    sum += i
    i += 1
print('10~100的总和为:',sum)

# while-else搭配
s = 'ABC'
i = 0
while i<len(s):
    print('循环进行中:'+s[i])
    i += 1
else:
    print("循环结束！")
