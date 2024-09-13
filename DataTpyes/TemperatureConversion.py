def convert_f_to_c(f, c):
    # celsius：摄氏温度
    celsius = (f - 32) / 1.8
    # fahrenheit:华氏温度
    fahrenheit = c * 1.8 + 32

    return celsius, fahrenheit


c = float(input("请输入要计算的摄氏温度:"))
f = float(input("请输入要计算的华氏温度:"))
a, b = convert_f_to_c(f, c)
print("%.2f摄氏温度 = %.2f华氏温度" % (c, b))
print("%.2f华氏温度 = %.2f摄氏温度" % (f, a))
