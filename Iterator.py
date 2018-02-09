# 可迭代对象 Iterable: 可以直接作用于for循环的对象
# 一类是集合数据类型，如list、tuple、dict、set、str等；
# 一类是generator，包括生成器和带yield的generator function。

# 迭代器 Iterator 可以被next()函数调用并不断返回下一个值的对象
# isinstance()判断一个对象是否是Iterator对象
# isinstance((x for x in range(10)), Iterator) True
# 使用iter()函数 将 Iterable变成Iterator
from collections import Iterator
L = isinstance([], Iterator)
print(L) # False
L = isinstance(iter([]), Iterator)
print(L) # True