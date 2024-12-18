
# PM2.5值1~35为优；35~75为良好;75以上为污染

# if-单分支结构
PM = eval(input('请输入PM2.5值:'))
if 0 <= PM < 35:
    print("空气质量优！")
if 35 <= PM <75:
    print('空气质量良好！')
if PM >= 75:
    print("空气污染！")


# if-else语句
PM2 = eval(input('请输入PM2.5值:'))
if PM2 < 75:
    print('适合户外运动！')
else:
    print('减少户外运动')

# 二分支结构
n = eval(input('请输入PM2.5值：'))
print('减少户外活动') if n >= 75 else print('适合户外运动')

# if-elif-else语句
PM3 = eval(input('请输入PM2.5值:'))
if 0 <= PM3 < 35:
    print("空气质量优！")
elif 35 <= PM3 <75:
    print('空气质量良好！')
else:
    print("空气污染！")