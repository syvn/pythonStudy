# 概念 一个无序不重复元素的序列。
# 创建 使用大括号 { } 或者 set() 函数创建集合
# 格式: 
# 	parame = {value01,value02,...}
# 	set(value) value 可以是list 或 tuple
student = {1, 2, 3, 4}
teacher = set((1, 2))
print(student, teacher) # {1, 2, 3, 4}

# 集合运算
a = set('abracadabra')
b = set('alacazam')
# 差集
print(a - b) # {'b', 'd', 'r'}

# 并集
print(a | b) # {'b', 'c', 'r', 'l', 'm', 'z', 'a', 'd'}

# 交集
print(a & b) # {'a', 'c'}

# 不同时存在
print(a ^ b) # {'l', 'b', 'm', 'z', 'd', 'r'}