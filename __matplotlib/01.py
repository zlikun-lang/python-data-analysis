import matplotlib.pyplot as plt
import numpy as np

## 图形一
# 生成一个Line2D对象，表示一条直线
line = plt.plot([1, 2, 3, 4])
# [<matplotlib.lines.Line2D object at 0x000002759A7AB4A8>]
print(line)
# 通过show()函数显示图表
# plt.show()

## 图形二
# 设置坐标系[x0, x1, y0, y1]
plt.axis([0, 5, 0, 20])
# 设置标题
plt.title('my first plot')
# 生成图形
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'ro')
# 显示图形
# plt.show()

## 图形三
# evenly sampled time at 200ms intervals
t = np.arange(0., 5., 0.2)
# red dashes, blue squares and green triangles
plt.plot(t, t, 'r--', t, t ** 2, 'bs', t, t ** 3, 'g^')


# plt.show()


## 图形四：生成多个子图
def f(t):
    return np.exp(-t) * np.cos(2 * np.pi * t)


t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

plt.figure(1)
plt.subplot(211)
plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

plt.subplot(212)
plt.plot(t2, np.cos(2 * np.pi * t2), 'r--')
plt.show()
