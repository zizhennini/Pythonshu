n = eval(input()) #获取n的值
########## Begin ##########
# 在Begin-End区间内补全代码
an = (n**2 - 1) / 2 if n % 2 != 0 else n**2 / 2
########## End ##########
print(int(an))    #打印大衍数列第n项的值an
