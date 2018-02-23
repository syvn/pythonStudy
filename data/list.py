# 声明一个 list
list1 = [1, 2, 3, 4]

# 取值
print(list1[1])
print(list1[1:2])

# 合并列表
print([1, 2, 3] + [2, 3, 4])

# 复制列表元素
print([[1, 2], 2] * 4) # [[1, 2], 2] + [] 四次加

# 遍历
for x in [1, 2, 3]:
	print(x, end = " ")

# 列表函数, 方法
# 
# 列表个数 len(list)

print(len([1, 2, 3])) # 3

# 最小值 min(list) 必须是同种类型数据
print(min(['1', '2'])) # 1

# 元祖 -> 列表
# list(seq)
print(list((1, 2, 3)))