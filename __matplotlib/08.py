import matplotlib.pyplot as plt
import numpy as np

## 生成条状图

index = np.arange(5)
values = [5., 7, 3, 4, 6]

# 垂直条状图
plt.bar(index, values, label='First')
plt.xticks(index, list('ABCDE'))
# plt.legend(['first series'])
# 如果生成图形时指定了label，生成图例时可以不指定名称
plt.legend()
plt.show()

# 水平条状图
plt.barh(index, values)
plt.legend(['first series'])
plt.yticks(index, list('ABCDE'))
plt.show()

# 多条条状图
values2 = [6., 6, 4, 5, 7]
values3 = [5., 6, 5, 4, 6]
bw = 0.2
plt.axis([0, 5, 0, 8])
plt.bar(index + bw, values, bw, color='r')
plt.bar(index + 2 * bw, values2, bw, color='g')
plt.bar(index + 3 * bw, values3, bw, color='b')
plt.xticks(index + 2 * bw, list('ABCDE'))
plt.show()
