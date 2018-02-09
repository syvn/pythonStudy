# 判断是否可以迭代
# str, list, tuple 可以迭代
# number 不可以迭代
from collections import Iterable
a = isinstance('abc', Iterable)
print(a)