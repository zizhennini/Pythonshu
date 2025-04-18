########## Begin ##########
import matplotlib.pyplot as plt #导入库
h, v0, g = 3000, 200, 9.8       #设置参数值
t = 0
tmax = (2*h / g)**0.5
delta = tmax / 29
xt = []
yt = []
while t <= tmax:
    xt.append(v0*t)                       #计算横坐标
    yt.append(h-1/2*g*t**2)
    t +=delta
for i in range(len(xt)):
    plt.plot(xt[i],yt[i],'ro')            #绘制点(xt,yt)
plt.grid('on')                  #显示网格线
plt.axis([0,5000,0,3000])          #设置坐标轴范围
plt.show()                      #显示图形
plt.savefig( 'step2/student/pic.png' )
plt.close()
