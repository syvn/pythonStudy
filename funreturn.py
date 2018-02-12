def lazy_sum(*args):
	def sum():
		ax = 0
		for n in args:
			ax += ax + n
		return ax
	return sum
f = lazy_sum(1, 3, 4, 5, 1)
L = f()
print(f, L)

def count():
	fs = []
	for i in range(1, 4):
		def f():
			return i * i
		fs.append(f)
	return fs
f1 = count()
print(f1[0]())

# 采用闭包
def count1():
	def f(j):
		def g():
			return j * j
		return g
	fs = []
	for i in range(1, 4):
		fs.append(f(i))
	return fs

f1, f2, f3 = count1()
print(f1())

def createCounter():
	fs = [0]
	def counter():
		fs[0] = fs[0] + 1
		return fs[0]
	return counter

counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())