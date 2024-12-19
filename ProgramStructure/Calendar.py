import prettytable as prettytable


# 判断是否为闰年
def leap_year(year):
    # 年份能被4整除且步能被100整除，或者能被400整除时为闰年
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return True
    else:
        return False


# 获取当月有几天
def month_days(year,month):
    if month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    elif month in [1,3,5,7,8,10,12]:
        return 31
    else:
        return 30

# 获取1990年到之后某一年的总天数
def total_days(year,month):
    days = 0
    for i in range(1990,year):
        if leap_year(i):
            days += 366
        else:
            days += 365
    for i in range(1,month):
        days += month_days(year,i)
    return days

if __name__=='__main__':
    year = eval(input("请输入指定年份:"))
    month = eval(input('请输入指定月份:'))
    print('\t\t{}年{}月份日历'.format(year,month))
    print('Sun\tMon\tTues\tWed\tThur\tFri\tsat')
    print('-------------------------------------------------')
    count = 0
    # 当前月份的1号是星期几
    for i in range((total_days(year,month)+1)%7):
        print(end='\t')
        count += 1
    for i in range(1,month_days(year,month)+1):
        print(i,end='\t')

        count += 1
        if count % 7 == 0:
            print()