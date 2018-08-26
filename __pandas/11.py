from pandas import DataFrame
import numpy as np

df = DataFrame([
    [1.4, np.nan],
    [7.1, -4.5],
    [np.nan, np.nan],
    [0.75, -1.3]
],
    index=list('abcd'),
    columns=['one', 'two']
)

#     one  two
# a  1.40  NaN
# b  7.10 -4.5
# c   NaN  NaN
# d  0.75 -1.3
print(df)

# 返回每列小计的Series
# one    9.25
# two   -5.80
# dtype: float64
print(df.sum())

# 按行计算（axis=0表示行、axis=1表示列），计算过程中，NaN值被自动排除
# a    1.40
# b    2.60
# c    0.00
# d   -0.55
# dtype: float64
print(df.sum(axis=1))

# 可以禁止排除，那么包含NaN的项计算结果都为NaN
# a     NaN
# b    2.60
# c     NaN
# d   -0.55
# dtype: float64
print(df.sum(axis=1, skipna=False))

# 一次产生多个汇总统计
#             one       two
# count  3.000000  2.000000     # 非NA值数量
# mean   3.083333 -2.900000     # 值的平均数
# std    3.493685  2.262742     # 样本值的标准差
# min    0.750000 -4.500000     # 计算最小值
# 25%    1.075000 -3.700000
# 50%    1.400000 -2.900000
# 75%    4.250000 -2.100000
# max    7.100000 -1.300000     # 计算最大值
print(df.describe())

# 其对应各分项
# one    3
# two    2
# dtype: int64
print(df.count())
# one    3.083333
# two   -2.900000
# dtype: float64
print(df.mean())
# one    3.493685
# two    2.262742
# dtype: float64
print(df.std())
# one    0.75
# two   -4.50
# dtype: float64
print(df.min())
# one    7.1
# two   -1.3
# dtype: float64
print(df.max())
# 计算百分数变化
#         one       two
# a       NaN       NaN
# b  4.071429       NaN
# c  0.000000  0.000000
# d -0.894366 -0.711111
print(df.pct_change())


