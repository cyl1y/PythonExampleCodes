
# try-except异常处理
'''
try:
    <语句块1>
except<异常类型>:
    <语句块2>
'''
try:
    num = eval(input('请输入一个整数:'))
    print(num*num)
except:
    print('输入错误，请输入整数')