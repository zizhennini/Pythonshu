"""
背景
　　辗转相除法也叫欧几里得算法，因为这个方法最先出现在古希腊数学家欧几里得的著作《几何原本》中。
　　辗转相除法的功能是快速计算两个正整数的最大公约数（下面只在正整数范围讨论）。一个整数 a 的约数是指能整除 a 的所有整数的集合，如 4 的约数有 1、2、4，6 的约数有 1、2、3、6。而两个整数 a 和 b 的公约数，是指它们共同的约数，如 4 和 6 的公约数是 1、2。而 a 和 b 的最大公约数就是公约数中的最大者，如 4 和 6 的最大公约数是 2。
　　最大公约数看似简单，其实在数论、密码学等很多领域有着重要的作用。而辗转相除法因为能比其它方法更快算出结果，所以在这些领域得到了广泛的应用，成为一些领域的基础算法之一。

任务
　　利用辗转相除法计算两个正整数 a 和 b 的最大公约数，过程如下：

　　① 令 c=a%b
　　② 若 c==0，则输出 b，算法结束
　　③ 否则，依次令 a=b、b=c、c=a%b
　　④ 重复步骤②和③
"""
a = int(input())
b = int(input())
########## Begin ##########
c = a % b
while c != 0:
    a = b
    b = c
    c = a % b
print(b)

########## End ##########