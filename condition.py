a = 3
if a > 10:
	print('a > 10')
elif a > 6:
	print('a > 6')
else:
	print('越界')

s = input('birth: ')
birth = int(s)
if birth < 2000:
	print('00前')
else:
	print('00后')