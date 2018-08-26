from pandas import Series, DataFrame

s1 = Series([7.3, -2.5, 3.4, 1.5], index=list('acde'))
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=list('acefg'))

# a    7.3
# c   -2.5
# d    3.4
# e    1.5
# dtype: float64
print(s1)

# a   -2.1
# c    3.6
# e   -1.5
# f    4.0
# g    3.1
# dtype: float64
print(s2)

# 两者相加，两边都存在则值相加，至少有一方不存在，则为NaN
# a    5.2
# c    1.1
# d    NaN
# e    0.0
# f    NaN
# g    NaN
# dtype: float64
print(s1 + s2)

# 如果需要对不重叠的位置使用填充，使用add方法中的fill_value参数实现
# 这种方式会以前者为主
# a    5.2
# c    1.1
# d    3.4
# e    0.0
# f    4.0
# g    3.1
# dtype: float64
print(s1.add(s2, fill_value=0))
