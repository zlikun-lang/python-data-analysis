from pandas import Series, DataFrame
import numpy as np

obj = Series(np.arange(5.), index=list('abcde'))

# a    0.0
# b    1.0
# c    2.0
# d    3.0
# e    4.0
# dtype: float64
print(obj)

# 丢弃指定轴上的项
obj2 = obj.drop('c')
# a    0.0
# b    1.0
# d    3.0
# e    4.0
# dtype: float64
print(obj2)

obj2 = obj.drop(['a', 'c'])
# b    1.0
# d    3.0
# e    4.0
# dtype: float64
print(obj2)

# 对DataFrame来说也可以删除任意轴上的索引值
frame = DataFrame(np.arange(16).reshape(4, 4), index=range(1, 5), columns=range(101, 105))
#    101  102  103  104
# 1    0    1    2    3
# 2    4    5    6    7
# 3    8    9   10   11
# 4   12   13   14   15
print(frame)

frame2 = frame.drop([1, 3])
#    101  102  103  104
# 2    4    5    6    7
# 4   12   13   14   15
print(frame2)

# 删除列则使用del关键字
del frame2[102]
#    101  103  104
# 2    4    6    7
# 4   12   14   15
print(frame2)

# 通过指定columns，也可以使用drop删除列
frame2 = frame.drop(columns=[101, 103])
#    102  104
# 1    1    3
# 2    5    7
# 3    9   11
# 4   13   15
print(frame2)
