n = input()
if '.' in n:
    n = float(n)
    print('%.1f' % abs(n))
else:
    n = int(n)
    print(abs(n))