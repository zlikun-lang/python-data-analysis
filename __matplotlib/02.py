import matplotlib.pyplot as plt

# 设置坐标系[x0, x1, y0, y1]
plt.axis([0, 5, 0, 20])
# 设置图形名称，通过参数设置样式
plt.title('my plot', fontsize=20, fontname='Times New Roman')
# 设置X轴、Y轴标签，通过color设置字体颜色
plt.xlabel('Counting', color='gray')
plt.ylabel('Square values', color='gray')
# 在图形中任意位置生成文本[x, y, text]
plt.text(1, 1.5, 'First')
plt.text(2, 4.5, 'Second')
plt.text(3, 9.5, 'Third')
plt.text(4, 16.5, 'Fourth')
# 插入公式
plt.text(1, 12, r'$y = x^2$', fontsize=20, bbox={'facecolor': 'yellow', 'alpha': 0.2})
# 添加网格
plt.grid(True)
# 生成图形，前两个参数指定x、y轴坐标值序列，第三个参数则指定点的样式
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')  # 红色实心圆点
plt.plot([1, 2, 3, 4], [0.8, 3.5, 8, 15], 'g^')  # 绿色三角形
plt.plot([1, 2, 3, 4], [0.5, 2.5, 4, 12], 'b*')  # 蓝色五角星
# 添加图例
plt.legend(['First series', 'Second series', 'Third series'], loc=4)
# 显示图形
# plt.show()

# 直接将图形保存为图片文件
plt.savefig(r'.data/02.png')
