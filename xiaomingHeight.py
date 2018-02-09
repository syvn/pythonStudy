weight = 80.5
height = 1.75
bem = weight / pow(height, 2)

if bem < 18.5:
	print('小明过轻')
elif bem < 25 and bem >=18.5:
	print('正常')
elif bem < 28 and bem >= 25:
	print('过重')
elif bem < 32 and bem >= 28:
	print('肥胖')
else:
	print('严重肥胖')