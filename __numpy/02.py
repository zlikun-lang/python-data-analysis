import numpy as np

# 创建数组
arr = np.array([2, 3, 4])
# [2 3 4]
print(arr)

# 通过元组创建数组
arr = np.array([('x', 'y', 'z'), (1, 2, 4, 8)])
# [('x', 'y', 'z') (1, 2, 4, 8)]
print(arr)

# 创建矩阵，矩阵也是数组的一种
# 通过元组生成零矩阵
arr = np.zeros((2, 3))
# [[0. 0. 0.]
#  [0. 0. 0.]]
print(arr)

# 生成三维的单位矩阵
arr = np.identity(3)
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]
print(arr)

# 生成每个元素都在[0, 1]之间的随机矩阵
# size参数的意义为两行三列
arr = np.random.random(size=(2, 3))
# [[0.18649495 0.3033121  0.17580926]
#  [0.7676864  0.38212693 0.74402436]]
print(arr)

# 查看数组属性
# 返回矩阵规格
# (2, 3)
print(arr.shape)
# 返回矩阵的秩
# 2
print(arr.ndim)
# 返回矩阵元素总数
# 6
print(arr.size)
# 返回矩阵元素数据类型
# float64
print(arr.dtype.name)

# 通过索引和切片访问数组元素
arr = np.array([1, 1, 2, 3, 5, 8])
# [1 1 2 3 5 8]
print(arr)
# [1 1]
print(arr[:2])
# [2]
print(arr[2:3])
# [1 2 5]
print(arr[::2])

# 生成一个矩阵（4 * 3）
arr = np.fromfunction(lambda x, y: 10 * x + y, (4, 3), dtype=int)
# [[ 0  1  2]
#  [10 11 12]
#  [20 21 22]
#  [30 31 32]]
print(arr)
# 返回矩阵指定位置元素
# 2 11 30
print(arr[0, 2], arr[1, 1], arr[3, 0])
# 切片，返回矩阵前两行
# [[ 0  1  2]
#  [10 11 12]]
print(arr[:2, :])
# 切片，返回矩阵第二列
# [[ 1]
#  [11]
#  [21]
#  [31]]
print(arr[:, 1:2])
# 索引，返回最后一行
# [30 31 32]
print(arr[-1])

# 通过迭代器访问矩阵
# [0 1 2]
# [10 11 12]
# [20 21 22]
# [30 31 32]
for row in arr:
    print(row)

# 输出矩阵全部元素
# 0	1	2	10	11	12	20	21	22	30	31	32
for item in arr.flat:
    print(item, sep=',', end='\t')
print()
