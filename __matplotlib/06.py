import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

# 指定全局字体（默认：['sans-serif']），解决中文乱码问题，并统一全局字体
matplotlib.rcParams['font.family'] = ['SimHei']

# 某班级ABCD四次考试成绩数据
data = DataFrame({
    '张三': [71, 87, 82, 95],
    '李四': [87, 63, 77, 48],
    '王五': [94, 76, 67, 62],
    '赵六': [81, 87, 72, 98],
}, index=list('ABCD'))

# assert data.shape[0] == 4  # 行数
# assert data.shape[1] == 4  # 列数

# from matplotlib import font_manager as fm
# 如果需要引入外部字段，可以通过该方法实现，zh_font可以直接被使用
# 如：plt.legend(prop=zh_font)
# zh_font = fm.FontProperties(fname='$font_path.ttf')

# 设置坐标系
# data.min().min() / data.max().max()，分别取整个数据集最大值、最小值
# [x0, x1, y0, y1]，因为是包含的，但行索引从0开始计，所以减一
plt.axis([0, data.shape[1] - 1, 0, 100])
# 生成图形
plt.plot(np.arange(data.shape[0]), data)
# 添加图例，因为有中文，需要设置字体
plt.legend(data, loc=0)
# 可以精确设置坐标值
plt.xticks(range(data.shape[0]), [r'${}$'.format(index) for index in data.index])
# 设置标题(中文需要支持中文的字体支持)
plt.title(u'成绩趋势')
# 显示网格
plt.grid(True)
# 显示图形
plt.show()
