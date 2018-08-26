from pandas import Series, DataFrame
import pandas as pd

obj = Series(list('cadaabbcc'))

# 0    c
# 1    a
# 2    d
# 3    a
# 4    a
# 5    b
# 6    b
# 7    c
# 8    c
# dtype: object
print(obj)

# 返回Series中惟一值数组（未排序）
uniques = obj.unique()
# ['c' 'a' 'd' 'b']
print(uniques)

# 返回每个值出现次数（统计），结果默认按降序排列
# c    3
# a    3
# b    2
# d    1
# dtype: int64
print(obj.value_counts())

# 判断矢量化集合的成员资格，可用于选取Series和DataFrame列中的数据子集
# 0     True
# 1    False
# 2    False
# 3    False
# 4    False
# 5     True
# 6     True
# 7     True
# 8     True
# dtype: bool
mask = obj.isin(['b', 'c'])
print(mask)

# 0    c
# 5    b
# 6    b
# 7    c
# 8    c
# dtype: object
print(obj[mask])

data = DataFrame({
    'A': [1, 3, 4, 3, 4],
    'B': [2, 3, 1, 2, 3],
    'C': [1, 5, 2, 4, 4]
})

#    A  B  C
# 0  1  2  1
# 1  3  3  5
# 2  4  1  2
# 3  3  2  4
# 4  4  3  4
print(data)

# 统计各值出现频率，注意行代表的是DataFrame中出现的所有值，而非原行索引
result = data.apply(pd.value_counts).fillna(0)
#      A    B    C
# 1  1.0  1.0  1.0
# 2  0.0  2.0  1.0
# 3  2.0  2.0  0.0
# 4  2.0  0.0  2.0
# 5  0.0  0.0  1.0
print(result)
