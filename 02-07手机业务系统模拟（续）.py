x1 = int(input())  # 获取第1次按键
x2 = int(input())  # 获取第2次按键
x3 = int(input())  # 获取第3次按键
########## Begin ##########
if x1 == 1:
    if x2 == 1:
        if x3 == 1:
            print("话费查询")
        elif x3 == 2:
            print("账单查询")
        elif x3 == 3:
            print("积分查询")
        else:
            print("无效的业务选择")
    if x2 == 2:
        print("流量查询")
elif x1 == 2:
    if x2 == 1:
        if x3 == 1:
            print("充值卡充值")
        elif x3 == 2:
            print("微信充值")
        else:
            print("无效的业务选择")
    if x2 == 2:
        if x3 == 1:
            print("4G流量")
        else:
            print("5G流量")
elif x1 == 3:
    print("人工服务")
else:
    print("无效的业务选择")

########## End ##########
