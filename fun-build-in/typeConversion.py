# 内置方法 类型转换

# int() 将 字符串或数字转换成整数
# 语法 class int(x, base=10)
print(int()) # 0 不传入参数时, 得到结果0

print(int(3)) # 3
print(int(3.1)) # 3

# float() 将整数和字符串转换成浮点数
print(float(1)) # 1.0
print(float()) # 0.0

print(complex(1, 2)) # 1 + 2j
print(complex('1+2j')) # 1 + 2j  '1+2j' + 前后无空格

# str() 将对象转化为适于人阅读的形式
# class str(object='')
s = 'demo'
print(str(s)) # demo
print(type(str({'demo': '1'}))) # "{'demo': '1'}"  <class 'str'>

# eval() 用来执行一个字符串表达式，并返回表达式的值
# eval(expression[, globals[, locals]])
# expression -- 表达式 使用引号引起来
# globals -- 变量作用域, 全局命名空间, 如果被提供, 则必须是一个字典对象
# locals -- 变量作用域, 局部命名空间, 如果被提供, 可以是任何映射对象

x = 7
print(eval('3 * x')) # 21
print(eval('pow(2, 2)')) # 4

list1 = [1, 1, 2, 3]
print(tuple(list1))