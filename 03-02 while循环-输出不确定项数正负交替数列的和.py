result, i = 0, 0  # 累加器置0
########## Begin #########
n = float(input())

while True:
    # i+=1
    if abs((-1) ** i / (2 * i + 1)) <= n:
        break
    else:

        result = result + (-1) ** i / (2 * i + 1)
    i += 1

########## End ##########
print(result)
print(result * 4)