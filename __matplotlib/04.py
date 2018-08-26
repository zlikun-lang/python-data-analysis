import matplotlib.pyplot as plt
import numpy as np

# 线性图，如：y = sin(n * x) / x
# 设置X轴
x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
# 生成图形（将三组数据图形绘制在同一个图形中）
plt.plot(x, np.sin(1 * x) / x, color='r')
plt.plot(x, np.sin(2 * x) / x, color='g')
plt.plot(x, np.sin(3 * x) / x, color='b')
# 插入公式
plt.text(-2 * np.pi, 2.5, r'$y = sin(n * x)/x$', fontsize=16, bbox={'facecolor': 'g', 'alpha': 0.2})
# 添加图例
plt.legend(['First series', 'Second series', 'Third series'], loc=0)
# 可以精确设置坐标值
# 符号PI的表示需要使用LaTeX表达式字符串，使用$$包围，前面使用r表示不转义
# 使用两个列表设置，第一个列表表示数值，第二个表示显示值
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1, 0, +1, +2, +3],
           [r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$'])
# 设置标题(中文需要支持中文的字体支持)
plt.title(u'正弦图形', fontname='SimHei')
# 显示图形
plt.show()
