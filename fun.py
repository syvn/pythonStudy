# def my_abs(x):
# 	if not isinstance(x, (int, float)):
# 		raise TypeError('bad operand Type')
# 	if x >= 0:
# 		return x
# 	else:
# 		return -x

# print(my_abs(-99))

import math

def move(x, y, step, angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx, ny

x, y = move(100, 100, 60, math.pi/6)
print(x, y)

L = []
n = 1
while n <=99:
	L.append(n)
	n += 2