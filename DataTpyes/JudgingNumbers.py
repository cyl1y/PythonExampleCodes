def judging_numbers(x):
    if x == 45:
        print("恭喜你猜对了")
    else:
        if x > 45:
            print("太大了")
        else:
            print("太小了")
    return


exam = int(input("请输入您的数字："))
judging_numbers(exam)