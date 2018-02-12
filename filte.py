# 筛选奇数
def is_odd(n):
	return n % 2 == 1
# filter(fun, objArr)
# fun 过滤函数
# objArr 过滤序列
L = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10]))
print(L)

# 筛选素数
# 计算素数的一个方法是埃氏筛法，它的算法理解起来非常简单：

# 首先，列出从2开始的所有自然数，构造一个序列：
# 		2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取序列的第一个数2，它一定是素数，然后用2把序列的2的倍数筛掉：
# 		3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数3，它一定是素数，然后用3把序列的3的倍数筛掉：
# 		5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 取新序列的第一个数5，然后用5把序列的5的倍数筛掉：
# 		7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ...
# 不断筛下去，就可以得到所有的素数
def _odd_iter():
	n = 1
	while True:
		n += 2
		yield n

# 定义筛选规则函数
def _not_divisible(n):
	return lambda x: x % n > 0

# 定义生成器
def primes():
	yield 2
	it = _odd_iter()
	while True:
		n = next(it)
		yield n
		it = filter(_not_divisible(n), it)

# 打印 所有选出的素数
for n in primes():
	if n < 100:
		print(n)
	else:
		break