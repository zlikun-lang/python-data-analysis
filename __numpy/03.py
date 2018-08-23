import numpy as np

m = np.array([[2, 1], [1, 2]])
n = np.array([[1, 2], [3, 4]])

# 数组运算，矩阵运算是相同位置上元素的计算
# [[3 3]
#  [4 6]]
print(m + n)
# [[ 1 -1]
#  [-2 -2]]
print(m - n)
# [[-1  1]
#  [ 2  2]]
print(n - m)
# [[ 1  4]
#  [ 9 16]]
print(n ** 2)

# 普通乘法
# [[2 2]
#  [3 8]]
print(m * n)
# 矩阵乘法
# [[ 5  8]
#  [ 7 10]]
print(np.dot(m, n))

# 转置
# [[1 3]
#  [2 4]]
print(n.T)

# 逆矩阵
# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(np.linalg.inv(n))

# 数组元素求和、最小值、最大值
# 6 10
print(m.sum(), n.sum())
# 2 4
print(m.max(), n.max())
# 1 1
print(m.min(), n.min())

# 按行累计求和
# [[2 3]
#  [1 3]]
print(m.cumsum(axis=1))
