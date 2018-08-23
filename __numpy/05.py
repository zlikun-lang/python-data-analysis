import numpy as np

# 数组的合并与分割
m = np.array([1, 2, 3, 4])
n = np.array([1, 2, 4, 8])

# 纵向合并数组，注意参数是一个元组
# [[1 2 3 4]
#  [1 2 4 8]]
print(np.vstack((m, n)))
# 横向合并数组
# [1 2 3 4 1 2 4 8]
print(np.hstack((m, n)))

arr = np.array([[1, 2, 3, 4], [1, 2, 4, 8]])
# 纵向分割
# [array([[1, 2, 3, 4]]), array([[1, 2, 4, 8]])]
print(np.vsplit(arr, 2))
# 横向分割
# [array([[1, 2],
#        [1, 2]]), array([[3, 4],
#        [4, 8]])]
print(np.hsplit(arr, 2))
