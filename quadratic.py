# 计算一元二次方程
import math
def quadratic(a, b, c):
	m = b * b - 4 * a * c
	if m >= 0:
		x = (-b + math.sqrt(m))/(2 * a)
		y = (-b - math.sqrt(m))/(2 * a)
		return x, y
	else:
		return 'No Answer'
print(quadratic(2, 3, 1))