import numpy as np

arr = np.array([2, 0, 1, 8, 0, 8, 2, 3])

# [2 0 1 8 0 8 2 3]
print(arr)
# <class 'numpy.ndarray'>
print(type(arr))

# [2 0]
print(arr[:2])
# 0 8
print(arr.min(), arr.max())

# 对数组排序，会直接改变数据
arr.sort()
# [0 0 1 2 2 3 8 8]
print(arr)

# 创建二维数组
arr = np.array([[1, 2, 3], [4, 5, 6]])
# [[1 2 3] [4 5 6]]
print(arr)
# 输出平方矩阵
# [[ 1  4  9] [16 25 36]]
print(arr * arr)

