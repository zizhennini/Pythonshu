n = int(input())
########## Begin ##########
for i in range(n):
    m = ' ' * (n-i-1)
    p = '*' * (2*i+1)
    print(m+p+m)
########## End ##########