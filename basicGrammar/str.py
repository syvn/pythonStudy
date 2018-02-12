str = '12345'
# 字符串截取 变量[头下标:尾下标] 从头下标开始, 到尾下标之前的字符(不包含尾下标位置字符)
print(str[0:2]) # 12 index >= 0 and index < 2
print(str[0:]) # 12345 index >= 0
print(str[:2]) # 12 index < 2

# 字符串连接 使用 + 号对字符串进行连接
print(str + 'text') # 12345text

# 字符串复制 使用 * 号对字符串进行复制 数字表示次数
print(str * 2) # 1234512345

# 转义字符
# \n 换行符
print('jacaScript\n111')
# javaScript
# 111
# 取消转义, 原样输出
print(r'javaScript\n111') # javaScript\n111

# 续行符
str = 'java'\
		'Script'
str = """'java'
		...'Script'"""
print(str) # javaScript