from pandas import Series

obj = Series(range(4), index=list('dabc'))

# d    0
# a    1
# b    2
# c    3
# dtype: int64
print(obj)

# 按索引排序
obj2 = obj.sort_index()
# a    1
# b    2
# c    3
# d    0
# dtype: int64
print(obj2)

# 还可以指定升序、降序排列
obj2 = obj.sort_index(ascending=False)
# d    0
# c    3
# b    2
# a    1
# dtype: int64
print(obj2)

# 按值排序（有些书上使用order方法，但当前版本的pandas并没有该方法）
obj2 = obj.sort_values()
# d    0
# a    1
# b    2
# c    3
# dtype: int64
print(obj2)
