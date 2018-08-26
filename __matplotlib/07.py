import matplotlib.pyplot as plt
import numpy as np

## 生成直方图

# 生成一个包含40个元素的在[0, 100]区间内的整数随机序列
pop = np.random.randint(0, 100, 40)
# print(pop)

# 使用该数据样本生成一个直方图
# bins指定面元数，默认：10
n, bins, patches = plt.hist(pop, bins=20)
# [2. 3. 0. 4. 0. 2. 1. 4. 2. 1. 3. 0. 1. 4. 0. 2. 4. 0. 3. 4.]
print(n)
# [ 2.    6.85 11.7  16.55 21.4  26.25 31.1  35.95 40.8  45.65 50.5  55.35
#  60.2  65.05 69.9  74.75 79.6  84.45 89.3  94.15 99.  ]
print(bins)
# <a list of 20 Patch objects>
print(patches)

# 显示图形
plt.show()
