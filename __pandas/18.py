from pandas import DataFrame, Series
import pandas as pd

df1 = DataFrame({
    'key': ['b', 'b', 'a', 'c', 'a', 'a', 'b'],
    'data1': range(7)
})
df2 = DataFrame({
    'key': ['a', 'b', 'd'],
    'data2': range(3)
})

#   key  data1
# 0   b      0
# 1   b      1
# 2   a      2
# 3   c      3
# 4   a      4
# 5   a      5
# 6   b      6
print(df1)
#   key  data2
# 0   a      0
# 1   b      1
# 2   d      2
print(df2)

# DataFrame合并
#   key  data1  data2
# 0   b      0      1
# 1   b      1      1
# 2   b      6      1
# 3   a      2      0
# 4   a      4      0
# 5   a      5      0
print(pd.merge(df1, df2, on='key'))
# 如果连接的键不同，可以显示指定
#   key  data1  data2
# 0   b      0      1
# 1   b      1      1
# 2   b      6      1
# 3   a      2      0
# 4   a      4      0
# 5   a      5      0
print(pd.merge(df1, df2, left_on='key', right_on='key'))
# 默认采用inner连接，还有left、right、outer,outer取得是并集
#   key  data1  data2
# 0   b    0.0    1.0
# 1   b    1.0    1.0
# 2   b    6.0    1.0
# 3   a    2.0    0.0
# 4   a    4.0    0.0
# 5   a    5.0    0.0
# 6   c    3.0    NaN
# 7   d    NaN    2.0
print(pd.merge(df1, df2, how='outer'))

# 如果合并DataFrame包含相同列，可以通过在重叠列名上添加后缀方式区分
df1['data'] = 128
#   key  data1  data
# 0   b      0   128
# 1   b      1   128
# 2   a      2   128
# 3   c      3   128
# 4   a      4   128
# 5   a      5   128
# 6   b      6   128
print(df1)

df2['data'] = -1
#   key  data2  data
# 0   a      0    -1
# 1   b      1    -1
# 2   d      2    -1
print(df2)

# 采用外连接方式连接
#   key  data1  data_left  data2  data_right
# 0   b    0.0      128.0    1.0        -1.0
# 1   b    1.0      128.0    1.0        -1.0
# 2   b    6.0      128.0    1.0        -1.0
# 3   a    2.0      128.0    0.0        -1.0
# 4   a    4.0      128.0    0.0        -1.0
# 5   a    5.0      128.0    0.0        -1.0
# 6   c    3.0      128.0    NaN         NaN
# 7   d    NaN        NaN    2.0        -1.0
print(pd.merge(df1, df2, how='outer', on='key', suffixes=('_left', '_right')))
