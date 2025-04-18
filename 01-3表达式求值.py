import math
a = float(input())
b = float(input())
c = float(input())
x = (-b + math.sqrt(b * b - 4*a*c)) / (2*a)
print(f'{x:.2f}')