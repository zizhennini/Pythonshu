########## Begin ##########
#在下一行编写代码，接收一个大于1的整数保存到n中
n = int(input())
result = 0  #累加器置0
#计算小于n的所有非负数的倒数和
for i in range(1,n,2):
    result = result + 1 / i

########## End ##########
print(result)