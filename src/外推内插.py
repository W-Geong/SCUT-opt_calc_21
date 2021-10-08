def 求单谷区间(f,起点,步长):
	if f(起点)>=f(起点+步长):

		if f(起点+步长)<f(起点+步长*3):
			return (起点,起点+步长*3)
		else:
			return 求单谷区间(f,起点+步长,2*步长)#消去左边
	else:
		if f(起点-步长)>f(起点):
			return (起点-步长,起点+步长)
		else:
			return 求单谷区间(f,起点-步长,2*步长)#消去右边

if __name__ == '__main__':
	求极小=True
	f=lambda x:x**3-x**2-30*x if 求极小 else -(x**3-x**2-30*x)#定义Inline函数
	# 起点=float(input("起点="))#过大的起点可能导致溢出
	# 步长=float(input("步长="))
	# print(求单谷区间(f,起点,步长))
	for 起点0 in [0, 2, 4, 6, 8]:
		print()
		for 步长 in [0.01, 0.05, 0.1, 0.5, 1]:
			if not 求极小: 起点0=-起点0
			起点,终点=求单谷区间(f,起点0,步长)
			print(f'起点为{起点0}，步长为{步长}时的单谷区间为({round(起点, 2)},{round(终点, 2)})，区间长度为：{round(终点-起点, 2)}')
