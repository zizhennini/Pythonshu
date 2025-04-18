x = eval(input())#获取小数x
########## Begin ##########
y = int(x)
z = x - y
if z>0.6:
    x_int = y + 1
else:
    x_int = y
########## End ##########
print(x_int)     #打印x对应的整数
