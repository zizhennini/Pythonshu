n = int(input())
########## Begin ##########
pi = 0
i = 0
for i in range(n):
    b = 4 * (-1) ** i * (1 / (2 * i + 1))

    pi += b

########## End ##########
print('%.6f' % pi)  # 圆周率= 3.1415926…