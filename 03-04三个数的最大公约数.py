a = int(input())
b = int(input())
c = int(input())
########## Begin ##########
from math import *
# 计算两个或多个整数的最大公约数，即能同时整除这些整数的最大正整数。例如，对于 12 和 18，其最大公约数为 6。
gcd_ab = gcd(a, b)
gcd_gc = gcd(gcd_ab, c)
print(gcd_gc)

########## End ##########