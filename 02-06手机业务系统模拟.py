"""
手机业务可以通过拨打服务电话进行办理，如移动用户拨打 10086、联通用户拨打 10010、电信用户拨打 10000 等。接通后，一般需要通过
多次 按键逐步选择对应业务。下表给出了某手机运营商业务办理系统中按键与业务的对应关系。
    第一次按键   第二次按键       业务
        1          1        话费查询
                   其它      账单查询
        其它        1        话费充值
                   其它      流量套餐
本关任务是模拟该业务办理系统，根据用户按键打印对应业务的名称（实际系统是调用对应的业务功能），
如用户第 1 次按键为 1、第 2 次按键为 3，则打印账单查询。
"""
x1 = int(input())  # 获取第1次按键
x2 = int(input())  # 获取第2次按键
########## Begin ##########
if x1 == 1:
    if x2 == 1:
        print("话费查询")
    elif x2 == 2:
        print("账单查询")
    else:
        print("无效的业务选择")
elif x1 == 2:
    if x2 == 1:
        print("话费充值")
    elif x2 == 2:
        print("流量套餐")
    else:
        print("无效的业务选择")
else:
    print("无效的业务选择")

########## End ##########
