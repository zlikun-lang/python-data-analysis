import numpy as np
from pandas import Series, DataFrame

obj = Series(np.arange(2001, 2005), index=list('abcd'))

# a    2001
# b    2002
# c    2003
# d    2004
# dtype: int32
print(obj)

# 使用索引获取值
assert obj[0] == 2001
assert obj[2] == 2003
# 使用指定索引，与使用数组下标效果一致
assert obj['a'] == obj[0]
assert obj['d'] == obj[-1]

# 索引切片
# b    2002
# c    2003
# dtype: int32
print(obj[1:3])

# 标签切片，与普通切片不同的是包含切片的末端值
# b    2002
# c    2003
# d    2004
# dtype: int32
print(obj['b':'d'])

# 某班级ABCD四次考试成绩数据
frame = DataFrame({
    '张三': [71, 82, 93, 95],
    '李四': [87, 63, 77, 48],
    '王五': [94, 76, 67, 62],
    '赵六': [81, 89, 78, 91],
}, index=list('ABCD'))

#    张三  李四  王五  赵六
# A  71  87  94  81
# B  82  63  76  89
# C  93  77  67  78
# D  95  48  62  91
print(frame)

# 取前两行[0, 2)
#    张三  李四  王五  赵六
# A  71  87  94  81
# B  82  63  76  89
print(frame[:2])

# 取指定列
# A    94
# B    76
# C    67
# D    62
# Name: 王五, dtype: int64
print(frame['王五'])

# 取指定行
#    张三  李四  王五  赵六
# A  71  87  94  81
print(frame[:1])
#    张三  李四  王五  赵六
# C  93  77  67  78
print(frame[2:3])
#    张三  李四  王五  赵六
# B  82  63  76  89
print(frame['B':'B'])

# 布尔型 DataFrame
#       张三     李四     王五     赵六
# A  False   True   True   True
# B   True  False  False   True
# C   True  False  False  False
# D   True  False  False   True
print(frame > 80)

# 通过布尔型DataFrame选取
#      张三    李四    王五    赵六
# A   NaN  87.0  94.0  81.0
# B  82.0   NaN   NaN  89.0
# C  93.0   NaN   NaN   NaN
# D  95.0   NaN   NaN  91.0
print(frame[frame > 80])

# 选取行（张三成绩大于80的行）
#    张三  李四  王五  赵六
# B  82  63  76  89
# C  93  77  67  78
# D  95  48  62  91
print(frame[frame['张三'] > 80])

# 使用loc/iloc方法（代替ix，该方法已废弃）可以简化切片、选取的用法
# 87，使用标签
print(frame.loc['A', '李四'])
# 87，使用索引（位置）
print(frame.iloc[0, 1])

# 实现切片
#    李四  王五
# A  87  94
# B  63  76
print(frame.loc['A':'B', '李四':'王五'])
