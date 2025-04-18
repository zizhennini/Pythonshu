"""
y={10-(x**4+4)*0.5, x<0/
y={8-6(x)*0.5,  0<=x<=1/
y={1+x**2          ,x>1/
"""
x = eval(input())   #获取x的值
########## Begin ##########
import math
if x<0:
    y=10-math.sqrt(x**4+4)
elif 0<=x<=1:
    y=8-6*math.sqrt(x)
else:
    y=1+x**2
########## End ##########
print('%.4f' % (y)) #打印函数值（保留4位小数）
