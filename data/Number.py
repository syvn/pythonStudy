var1 = 1
var2 = 2

# 删除数字对象的引用
print(var1) # 1
# del var1
# print(var1) # NameError: name 'var1' is not defined

# 类型转换
# 
# int(x) 将x转换为一个整数。
# float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

num = 1
print(float(num)) # 1.0

print(complex(num)) # 1+0j

# 引入数学运算模块
import math

# 幂运算
#  ** 幂次方
print(5 ** 2) # 平分
print(5 ** 7) # 7次方

print(abs(-1)) # 绝对值
print(math.ceil(1.3)) # 向上取整 2

# 向下取整
print(math.floor(1.3)) # 1

# 取自然对数
# log(x)

# 取对数
# log10(x) 10 为基数

# 最大值
# 参数可为序列, 元祖
print('max:', max(1, 1, 2, 3))
print('max:', max([1, 1, 2, 3]))
print('max:', max((1, 1, 2, 3)))

# 返回整数和小数组合 tuple
print(math.modf(1.2))

print('x ** y:', math.pow(2.13, 2))