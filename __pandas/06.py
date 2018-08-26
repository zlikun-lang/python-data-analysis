import numpy as np
from pandas import Series, DataFrame

# 通过列表构造一个Series，指定其索引，两者数量必须匹配
obj = Series([4.5, 7.2, -5.3, 3.6], index=['a', 'b', 'c', 'd'])

# a    4.5
# b    7.2
# c   -5.3
# d    3.6
# dtype: float64
print(obj)

# 重新索引，缺失项由NaN填充
obj2 = obj.reindex(['a', 'b', 'c', 'm', 'n'])
# a    4.5
# b    7.2
# c   -5.3
# m    NaN
# n    NaN
# dtype: float64
print(obj2)

# 缺失位可以用指定值填充
obj2 = obj.reindex(['a', 'b', 'c', 'm', 'n'], fill_value=0)
# a    4.5
# b    7.2
# c   -5.3
# m    0.0
# n    0.0
# dtype: float64
print(obj2)

obj = Series(['red', 'green', 'blue'], index=[0, 2, 4])
# 0      red
# 2    green
# 4     blue
# dtype: object
print(obj)

# 使用method做插值处理，ffill/pad表示前填充，bfill/backfill表示向后填充
obj2 = obj.reindex(range(6), method='ffill')
# 0      red
# 1      red
# 2    green
# 3    green
# 4     blue
# 5     blue
# dtype: object
print(obj2)

obj2 = obj.reindex(range(6), method='bfill')
# 0      red
# 1    green
# 2    green
# 3     blue
# 4     blue
# 5      NaN
# dtype: object
print(obj2)

# 使用数组构造DataFrame，指定索引和列
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'c', 'd'], columns=['A', 'B', 'C'])
#    A  B  C
# a  0  1  2
# c  3  4  5
# d  6  7  8
print(frame)

# 重新索引
frame2 = frame.reindex(['a', 'b', 'c', 'd'])
#      A    B    C
# a  0.0  1.0  2.0
# b  NaN  NaN  NaN
# c  3.0  4.0  5.0
# d  6.0  7.0  8.0
print(frame2)

# 也可以对列重新生成，通过columns字段指定
frame2 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'])
#      A    B    C   D
# a  0.0  1.0  2.0 NaN
# b  NaN  NaN  NaN NaN
# c  3.0  4.0  5.0 NaN
# d  6.0  7.0  8.0 NaN
print(frame2)

# DataFrame也可以进行插值填充，但只能针对行填充，不能针对列填充
frame2 = frame.reindex(index=['a', 'b', 'c', 'd'], columns=['A', 'B', 'C', 'D'], method='bfill')
#    A  B  C   D
# a  0  1  2 NaN
# b  3  4  5 NaN
# c  3  4  5 NaN
# d  6  7  8 NaN
print(frame2)
