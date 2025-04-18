########## Begin ##########
s = 0
m = 1000
for n in range(1, m + 1):
    s = 0
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            s += i
    if s == n:
        print(n)

########## End ##########