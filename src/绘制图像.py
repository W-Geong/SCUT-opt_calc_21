from matplotlib import pyplot as plt  
import numpy as np  

f=lambda x:x**3-x**2-30*x#定义Inline函数

start=-10 #输入需要绘制的起始值（从左到右）
stop=10 #输入需要绘制的终点值
num=100 #计算100个点

x = np.linspace(start,stop,num)
y = f(x)

plt.plot(x, y,label=r'$f(x)=x^3-x^2-30x$')#在当前的对象上进行操作
plt.grid(True)#显示网格
plt.legend()#显示旁注#注意：不会显示后来再定义的旁注
plt.show()#没有输入值默认展示所有对象
