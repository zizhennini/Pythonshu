"""
利用方括号、range函数可以创建列表，其实创建列表还有一种更强大、更方便的方法，就是使用 for 语句，这样就可以以一种更简单的方法绘
制轨迹，本关任务就是学习它的使用方法。

相关知识
语法
　　之前学到，for 语句的语法格式是：

for x in 序列
　　这里的序列可以是一个列表，也可以是range函数，还可以是其它对象，表示对序列里面的每一个元素 x 分别进行一些处理。
　　而利用 for 语句创建列表的方法，就是在此基础上，再加一个包含 x 的表达式，就能构建出新的列表 L：

L = [包含x的表达式 for x in 序列]
　　构建的过程是将序列里面的每个元素x分别代入表达式进行计算，如果序列里面有 n 个元素，就将这 n 个元素分别代入表达式，得到 n 个新
的值，这 n 个值就构成了新的列表L。
"""
#第1题
L = [101, 25, 38, 29, 108]
########## Begin ##########
s1=0
for i in range(len(L)):
    s1 =s1 + L[i]**2


########## End ##########
print(s1)           #打印s1

#第2题
########## Begin ##########
s2 = 0
for i in range(1,11):
    s2 =s2 +(1/i**2)

########## End ##########
print('%.5f' % s2)  #打印s2（保留5位小数）

