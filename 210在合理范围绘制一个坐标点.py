########## Begin ##########
import math
import matplotlib.pyplot as plt #导入库
h, v0, g = 3000, 200, 9.8       #设置参数值
t = eval(input())
if t<0 or t>math.sqrt(2*h/g):
    print('输入错误')
else:                   #读取时刻t
    print('绘制坐标')
xt = v0*t                       #计算横坐标
yt = h-1/2*g*t**2               #计算纵坐标
plt.plot(xt,yt,'ro')            #绘制点(xt,yt)
plt.grid('on')                  #显示网格线
plt.axis([0,5000,0,h])          #设置坐标轴范围
plt.show()                           #显示图形
########## End ##########

plt.savefig( 'src/step2/student/pic.png' )
plt.close()