# 生成器
L = [x * x for x in range(10)]
print(L)
g = (x * x for x in range(10))
for n in g:
	print(n)

# 斐波拉契数列 Fibonacci
# 如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
def fib(max):
	print('begain')
	n, a, b = 0, 0, 1
	while n < max:
		yield(b)
		a, b = b, a + b
		n += 1
	return 'done'
print(fib(10))

def odd():
	print('step 1')
	yield 1
	print('step 2')
	yield(3)
o = odd()
next(o)