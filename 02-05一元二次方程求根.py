a = eval(input())  # 获取a的值
b = eval(input())  # 获取b的值
c = eval(input())  # 获取c的值
########## Begin ##########
import math

n = b ** 2 - 4 * a * c
if n > 0:
    x1 = (-b + math.sqrt(n)) / (2 * a)
    x2 = (-b - math.sqrt(n)) / (2 * a)
    print('x1=%.4f,x2=%.4f ' % (x1, x2))
elif n == 0:
    x1 = (-b) / (2 * a)
    print('x1=%.4f' % (x1))
else:
    print("无实数根")

########## End ##########
