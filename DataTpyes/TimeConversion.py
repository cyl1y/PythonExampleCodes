def convert_seconds_to_time(t):
    # 计算时分秒
    hours = t // 3600
    minutes = (t % 3600) // 60
    seconds = t % 60
    # 返回格式化的时间字符串
    return f"{hours:d}:{minutes:d}:{seconds:d}"


# 实列使用
t = int(input("请输入秒数:"))
time_conversion = convert_seconds_to_time(t)
print("H:M:S =",time_conversion)
