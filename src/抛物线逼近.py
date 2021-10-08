import numpy as np
def 求解线性方程组(f,x1,x2,x3):
	A = np.array([[x1**2, x1, 1], [x2**2, x2, 1], [x3**2, x3, 1]])  # A代表系数矩阵
	b = np.array([f(x1), f(x2), f(x3)])  # b代表常数列
	x = np.linalg.solve(A, b)
	return -x[1]/(2*x[0])

def 抛物线逼近(f,起点,终点,精度):
	x1=起点;x2=(起点+终点)/2;x3=终点
	assert x1<x2 and x2<x3 ,'x的值必须从小到大'
	assert f(x1)>f(x2) and f(x3)>f(x2) ,'必须构成两边高，中间低的“极小化框架”'
	xp=求解线性方程组(f,x1,x2,x3)#计算xp初始值

	while abs(x2-xp)>=精度:
		if f(xp)>f(x2):
			if xp>x2:
				x3=xp
			else:
				x1=xp
		else:
			if xp>x2:
				x1=x2
				x2=xp
			else:
				x3=x2
				x2=xp
		xp=求解线性方程组(f,x1,x2,x3)#更新xp的位置

	return xp

if __name__ == '__main__':
	求极小=True
	f=lambda x:x**3-x**2-30*x if 求极小 else -(x**3-x**2-30*x)#定义Inline函数
	if 求极小:
		print(抛物线逼近(f,起点=3.3,终点=4.1,精度=1e-8))
	else:
		print(抛物线逼近(f,起点=-3.27,终点=-1.99,精度=1e-8))

