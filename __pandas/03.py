from pandas import Series

obj = Series([4, 7, -5, 3], dtype=int)

# 0    4
# 1    7
# 2   -5
# 3    3
# dtype: int32
print(obj)

# [ 4  7 -5  3]
print(obj.values)

# RangeIndex(start=0, stop=4, step=1)
print(obj.index)

obj = Series([4, 7, -5, 3], index=['a', 'b', 'c', 'd'])
# a    4
# b    7
# c   -5
# d    3
# dtype: int64
print(obj)

# -5
print(obj['c'])
# a    4
# b    7
print(obj[:2])

# a     True
# b     True
# c    False
# d     True
# dtype: bool
print(obj > 0)
# a    4
# b    7
# d    3
# dtype: int64
print(obj[obj > 0])

# True
print('b' in obj)

# 通过数据字典生成Series
# 通过字典生成的Series，字典的键即为索引
obj = Series({'id': 128, 'name': 'Jane', 'age': 17})
# id       128
# name    Jane
# age       17
# dtype: object
print(obj)

# 如果指定的索引在字典中不存在，则以NaN填充，表示不是一个数字，Series索引的顺序由index参数指定
obj = Series({'id': 128, 'name': 'Jane', 'age': 17}, index=['id', 'age', 'name', 'mobile'])
# id         128
# age         17
# name      Jane
# mobile     NaN
# dtype: object
print(obj)

# id        False
# age       False
# name      False
# mobile     True
# dtype: bool
print(obj.isnull())

# Series对象本身及其索引都有一个name属性，可以通过赋值设置
obj.name = 'my-series'
obj.index.name = 'my-series-state'
# my-series-state
# id         128
# age         17
# name      Jane
# mobile     NaN
# Name: my-series, dtype: object
print(obj)
