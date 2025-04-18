"""披萨的尺寸一般分6-15英寸几种，一英寸约等于2.54厘米，将英寸直径乘以2.54即可得出以厘米为单位的直径。
例如6寸披萨，即为6乘以2.54，得出结果为15.24厘米。 然而披萨加工时并不是严格到毫米不差的，考虑到加工过
程及无效的披萨边，真正的有效直径需要去掉小数点后面数字。例如6寸披萨的标准直径为15.24厘米，实际有效直径
一般为15厘米。披萨店经常会对顾客说：您订购的某尺寸的披萨卖完了，是否可以更换为多个小尺寸的披萨。例如：
您订购的9寸披萨卖完了，可以给您2个6寸的披萨吗？假设披萨厚度相同，价格与面积成正比，试问一个m英寸的大披
萨至少要更换几个n英寸的小披萨，顾客才不吃亏？"""

import math


# 定义计算披萨面积的函数
def pizza_area(diameter):
    radius = diameter / 2
    return math.pi * radius ** 2


# 读取输入
m = int(input())
n = int(input())

# 计算m英寸和n英寸披萨的面积
area_m_inch = pizza_area(m)
area_n_inch = pizza_area(n)

# 计算至少需要多少个n英寸的披萨来等于或超过一个m英寸的披萨面积
number_of_n_inch_pizzas = math.ceil(area_m_inch / area_n_inch)

# 输出结果
print(number_of_n_inch_pizzas)
