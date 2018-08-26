import matplotlib.pyplot as plt
import numpy as np

# 使用笛卡尔坐标系显示图形
# 线性图，如：y = sin(n * x) / x
# 设置X轴
x = np.arange(-2 * np.pi, 2 * np.pi, 0.01)
# 生成图形（将三组数据图形绘制在同一个图形中）
plt.plot(x, np.sin(1 * x) / x, color='r')
plt.plot(x, np.sin(2 * x) / x, color='g')
plt.plot(x, np.sin(3 * x) / x, color='b')
# 插入公式
plt.text(-2 * np.pi, 2.5, r'$y = \frac{\sin(n * x)}{x}$', fontsize=16, bbox={'facecolor': 'g', 'alpha': 0.2})
# 添加图例
plt.legend(['n = 1', 'n = 2', 'n = 3'], loc=0)
# 可以精确设置坐标值
# 符号PI的表示需要使用LaTeX表达式字符串，使用$$包围，前面使用r表示不转义
# 使用两个列表设置，第一个列表表示数值，第二个表示显示值
plt.xticks([-2 * np.pi, -np.pi, 0, np.pi, 2 * np.pi],
           [r'$-2\pi$', r'$-\pi$', r'$0$', r'$+\pi$', r'$+2\pi$'])
plt.yticks([-1, 0, +1, +2, +3],
           [r'$-1$', r'$0$', r'$+1$', r'$+2$', r'$+3$'])
# 设置标题(中文需要支持中文的字体支持)
plt.title(u'正弦图形', fontname='SimHei')
# 添加注释，使用annotate()函数实现，其包含LaTeX表达式，arrowprops属性指定箭头属性
plt.annotate(r'$\lim_{x\to 0}\frac{\sin(x)}{x}= 1$',
             xy=[0, 1],
             xycoords='data',
             xytext=[30, 30],
             fontsize=16,
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.2"))
# 使用笛卡尔坐标系
ax = plt.gca()
# 隐藏右边、上边的边框
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 将底边设置为X轴
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 将左边设置为Y轴
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
# 显示图形
plt.show()
