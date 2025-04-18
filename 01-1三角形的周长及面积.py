a = float(input())
b = float(input())
c = float(input())
l = a + b + c
s = (a + b + c) / 2
import math
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
# 获得三角形三条边长
round(l,2),round(area,2)
print(f"周长={l:.2f}\n面积={area:.2f}")

# 计算三角形面积和周长并输