y = int(input())    #获取年份
m = int(input())    #获取月份
########## Begin ##########
if m in [1,3,5,7,8,10,12]:
    print(31)
elif m in [4,6,9,11]:
    print(30)
elif m==2:
    if (y%4==0 and y%100!=0) or (y % 400 ==0):
        print(29)
    else:
        print(28)
else:
    print("该月份不存在")


########## End ##########
