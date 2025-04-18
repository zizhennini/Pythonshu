import math
a =float(input())
b =float (input())
x = (-b + math.sqrt(2*a*math.sin(math.radians(60))*math.cos(math.radians(60)))) / (2*a)

print(f'{x:.2f}')