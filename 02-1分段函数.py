x = int(input())
if -10 <= x < 0:
    y = 2 * x ** 3 + 4 * x ** 2 + 3
    print(y)
elif 0 <= x < 6:
    y = x + 14
    print(y)
elif 6 <= x <= 10:
    y = 6 * x
    print(y)
else:
    print("ERROR")
