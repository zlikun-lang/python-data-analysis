import numpy as np

arr = np.random.random((3, 4))
# [[0.49333691 0.86597875 0.48136798 0.3394656 ]
#  [0.93350547 0.1768723  0.72943248 0.8489749 ]
#  [0.12521165 0.27487904 0.59106752 0.56646613]]
print(arr)

# 布尔数组
# [[ True False  True  True]
#  [False  True False False]
#  [ True  True False False]]
print(arr < 0.5)

# 抽取小于0.5的元素，构成一个新数组
# [0.14366714 0.23697545 0.49979901 0.14402031]
print(arr[arr < 0.5])

# 数组复制
arr2 = arr.copy()
arr2[1, 1] = 4
# 0.7767376456502171 4.0
print(arr[1, 1], arr2[1, 1])
