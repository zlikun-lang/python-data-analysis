from pandas import Series, DataFrame
import numpy as np

string_data = Series(['a', 'b', np.nan, 'd'])
# 0      a
# 1      b
# 2    NaN
# 3      d
# dtype: object
print(string_data)

# 判断空值（缺失项）
# 0    False
# 1    False
# 2     True
# 3    False
# dtype: bool
print(string_data.isnull())

# Python中的None也被作为空值处理
string_data[0] = None
# 0     True
# 1    False
# 2     True
# 3    False
# dtype: bool
print(string_data.isnull())

# 对于NA值的处理方法

# 1、 dropna，删除NA值，返回一个不包含NA值的Series
# 1    b
# 3    d
# dtype: object
print(string_data.dropna())
# 使用布尔型索引也能实现该功能
# 1    b
# 3    d
# dtype: object
print(string_data[string_data.notnull()])

# 对于DataFrame而言，处理方式则要复杂一些，dropna默认丢弃任何包含有缺失值的行
data = DataFrame([
    [1., 6.5, 3.],
    [1., np.nan, np.nan],
    [np.nan, np.nan, np.nan],
    [np.nan, 6.5, 3.]
])
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  6.5  3.0
print(data)

# 可以看出所有包含NA的行都被删除了
#      0    1    2
# 0  1.0  6.5  3.0
print(data.dropna())
# 也可以按列删除，本例中全部列被删除了
# Empty DataFrame
# Columns: []
# Index: [0, 1, 2, 3]
print(data.dropna(axis=1))

# 如果只删除全部为NA的行（列）
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 3  NaN  6.5  3.0
print(data.dropna(how='all'))
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  NaN  NaN
# 2  NaN  NaN  NaN
# 3  NaN  6.5  3.0
print(data.dropna(how='all', axis=1))

# 2、 fillna，使用填充方式处理NA值
# 使用0填充所有NA值
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  0.0  0.0
# 2  0.0  0.0  0.0
# 3  0.0  6.5  3.0
print(data.fillna(0))

# 可以通过一个字典来填充，按列索引填充
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0  0.5 -1.0
# 2  NaN  0.5 -1.0
# 3  NaN  6.5  3.0
print(data.fillna({1: 0.5, 2: -1.}))

# 通过inplace=True，使修改应用到当前DataFrame（默认不修改，通过返回方式实现）
data.fillna({1: -1}, inplace=True)
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0 -1.0  NaN
# 2  NaN -1.0  NaN
# 3  NaN  6.5  3.0
print(data)

# 对reindex有效的那些插值方法，也适用于fillna方法
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0 -1.0  3.0
# 2  1.0 -1.0  3.0
# 3  1.0  6.5  3.0
print(data.fillna(method='ffill'))
#      0    1    2
# 0  1.0  6.5  3.0
# 1  1.0 -1.0  3.0
# 2  NaN -1.0  3.0
# 3  NaN  6.5  3.0
print(data.fillna(method='bfill'))
