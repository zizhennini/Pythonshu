"""
本关任务是在之前代码的基础上，利用“用 for 语句创建列表”的方法，更简单地绘制一条轨迹。

相关知识
　　第4关的绘制方法和本关的绘制方法，其区别在于列表xt和yt的构建过程。
　　之前是先构建两个空列表，再使用循环依次处理每个时刻，对于某个时刻t，计算该时刻的横坐标和纵坐标，分别追加到两个列表中，
循环 n 次后，就形成了 n 个时刻的坐标。
　　而本关创建xt和yt的过程为：
　　1）构造列表T，T中存放 n 个时刻，第 i 个时刻为i*delta，（i=0,1,2,…,n−1）；
　　2）从T出发得到列表xt，xt中存放了 n 个时刻的横坐标；
　　3）从T出发得到列表yt，yt中存放了 n 个时刻的纵坐标。
　　以上三个步骤都可以使用“用 for 语句创建列表”的方法。
"""

import matplotlib.pyplot as plt
h, v0, g = 3000, 200, 9.8
n = 30
tmax=(2*h/g)**0.5
delta = tmax/(n-1)
########## Begin ##########
xt,yt=[],[]
t = 0
while t<=tmax:
    xt.append(v0*t)
    yt.append(h-1/2*g*t**2)
    t = t + delta

########## End ##########
plt.plot(xt,yt,'r-')
plt.grid('on')
plt.axis([0, 5000, 0, h])
plt.show()
plt.savefig( 'src/step6/student/pic.png' )
plt.close()