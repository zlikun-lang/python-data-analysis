import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame

## 生成条状图


# 指定全局字体（默认：['sans-serif']），解决中文乱码问题，并统一全局字体
matplotlib.rcParams['font.family'] = ['SimHei']

data = DataFrame({
    '张三': [71, 87, 82, 95],
    '李四': [87, 63, 77, 48],
    '王五': [94, 76, 67, 62],
    '赵六': [81, 87, 72, 98],
}, index=list('ABCD'))

# 生成条状图
data.plot(kind='bar')
plt.show()
