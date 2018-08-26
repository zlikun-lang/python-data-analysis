import matplotlib
import matplotlib.pyplot as plt
from pandas import DataFrame

## 生成饼图


# 指定全局字体（默认：['sans-serif']），解决中文乱码问题，并统一全局字体
matplotlib.rcParams['font.family'] = ['SimHei']

labels = ['Nokia', 'Samsung', 'Apple', 'Lumia']
values = [10, 30, 45, 15]
colors = ['yellow', 'green', 'red', 'blue']

plt.pie(values,
        labels=labels,  # 标签列表
        colors=colors,  # 颜色列表
        # 表示将其中一块抽出[0, 1]，1表示完全抽出
        # 该列表对应labels，对应每个label抽出值
        explode=[0.3, 0, 0, 0],
        shadow=True,  # 显示阴影
        autopct='%1.1f%%',  # 显示百分比
        startangle=180  # 调整饼图旋转角度
        )
plt.axis('equal')
plt.show()

# 指定全局字体（默认：['sans-serif']），解决中文乱码问题，并统一全局字体
matplotlib.rcParams['font.family'] = ['SimHei']

# Pandas生成饼图
data = DataFrame({
    '张三': [71, 87, 82, 95],
    '李四': [87, 63, 77, 48],
    '王五': [94, 76, 67, 62],
    '赵六': [81, 87, 72, 98],
}, index=list('ABCD'))

# 针对一列生成饼图
data['张三'].plot(kind='pie', figsize=(6, 6))
plt.show()
