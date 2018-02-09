# 列表生成式
# 生成list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listDemo = list(range(1, 11))
print(listDemo) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 生成[1x1, 2x2, 3x3, ..., 10x10]
# 原 使用循环
L = []
for x in range(1, 11):
	L.append(x * x)
print(L) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# now 使用列表生成式 使用 x * x 代替 x 生成数字
# 执行顺序 for x in range(1, 11) -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# x * x for [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] -> [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
L = [x * x for x in range(1, 11)]
print(L) # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 筛选 偶数的平分
L = [x * x for x in range(1, 11) if x % 2 == 0]
print(L)

# 筛选 奇数的平分
L = [x * x for x in range(1, 11) if x % 2 != 0]
print(L)

# 多层循环
# for n in 'XYZ' -> [X, Y, Z]
# for m in 'ABC' -> [A, B, C]
# return L.append(m + n)
L = [m + n for m in 'ABC' for n in 'XYZ']
print(L) # ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 相当于循环的嵌套
L = []
for m in 'ABC':
	for n in 'XYZ':
		L.append(m + n)
print(L)

# 导入os模块
import os

# 查找当前文件目录 文件名列表
L = [d for d in os.listdir('.')]
print(L) # ['.git', 'condition.py', 'cycle.py', 'fun.py', 'hello.py', 'iterable.py', 'listComprehensions.py', 'power.py', 'quadratic.py', 'README.md', 'slice.py', 'while.py', 'xiaomingHeight.py']

# 练习
L = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L if isinstance(s, str)]
print(L2)

# 测试
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')