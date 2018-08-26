from pandas import Series, DataFrame, MultiIndex
import numpy as np

# 层次化索引
data = Series(np.random.randn(10),
              index=[
                  list('aaabbbccdd'),
                  [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]
              ])

# a  1    0.013618
#    2    0.193319
#    3   -0.122124
# b  1   -0.422517
#    2    1.210760
#    3    0.809057
# c  1    0.041199
#    2   -1.740763
# d  2   -0.019190
#    3   -1.387717
# dtype: float64
print(data)

# 查看索引信息
# MultiIndex(levels=[['a', 'b', 'c', 'd'], [1, 2, 3]],
#            labels=[[0, 0, 0, 1, 1, 1, 2, 2, 3, 3], [0, 1, 2, 0, 1, 2, 0, 1, 1, 2]])
print(data.index)

# 选取数据子集
# 1    0.560119
# 2   -0.047432
# 3    1.656930
# dtype: float64
print(data['b'])

# 切片也与普通索引没有什么分别
# b  1   -0.625102
#    2    1.407324
#    3   -0.254631
# c  1    0.355554
#    2   -1.550850
# dtype: float64
print(data['b':'c'])

# 区别在于可以进行内层选取
# a    0.572475
# b    1.266865
# c    0.518749
# dtype: float64
print(data[:, 1])
# -0.18287181968818497，浮点数自身的问题
print(data['b', 1])

# 复合索引的好处在于可以重塑和基于分组的操作
# 如：通过unstack方法将数据重新安排到一个DataFrame中
#           1         2         3
# a -1.057012  1.984407  1.274566
# b -2.580526 -1.015496 -1.499162
# c  0.039166  0.192631       NaN
# d       NaN  0.973031  0.174569
print(data.unstack())
# unstack的逆运算是stack
# a  1    0.681992
#    2   -0.485992
#    3    2.335656
# b  1    0.319687
#    2   -1.510173
#    3    0.401170
# c  1    0.335121
#    2    1.782211
# d  2    1.331409
#    3   -0.908997
# dtype: float64
print(data.unstack().stack())

# 如果是DataFrame，其每条轴都可以有分层索引
frame = DataFrame(np.arange(12).reshape(4, 3),
                  index=[
                      ['a', 'a', 'b', 'b'],
                      [1, 2, 1, 2]
                  ],
                  columns=[
                      ['Ohio', 'Ohio', 'Colorado'],
                      ['Green', 'Red', 'Green']
                  ])

#      Ohio     Colorado
#     Green Red    Green
# a 1     0   1        2
#   2     3   4        5
# b 1     6   7        8
#   2     9  10       11
print(frame)

# 注意索引和轴标签并不是一回事
frame.index.names = ['key1', 'key2']
frame.columns.names = ['state', 'color']

# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11
print(frame)

# 可以分组选取数据（按列选取使用列标签）
# color      Green  Red
# key1 key2
# a    1         0    1
#      2         3    4
# b    1         6    7
#      2         9   10
print(frame['Ohio'])

# 按行选取（必须使用切片方式）
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# b    1        6   7        8
#      2        9  10       11
print(frame['b':'b'])

# MultiIndex可以被创建并复用
multi_index = MultiIndex.from_arrays([
    ['Ohio', 'Ohio', 'Colorado'],
    ['Green', 'Red', 'Green']
], names=['state', 'color'])

# MultiIndex(levels=[['Colorado', 'Ohio'], ['Green', 'Red']],
#            labels=[[1, 1, 0], [0, 1, 0]],
#            names=['state', 'color'])
print(multi_index)

# swaplevel接收两个级别编号或名称，返回一个互换了级别（内外层索引交换）的新对象，值不变化
# state      Ohio     Colorado
# color     Green Red    Green
# key1 key2
# a    1        0   1        2
#      2        3   4        5
# b    1        6   7        8
#      2        9  10       11
print(frame)
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
# 2    a        3   4        5
# 1    b        6   7        8
# 2    b        9  10       11
print(frame.swaplevel('key1', 'key2'))
# 交换并排序（如果是使用索引，按交换后的索引来算）
# state      Ohio     Colorado
# color     Green Red    Green
# key2 key1
# 1    a        0   1        2
#      b        6   7        8
# 2    a        3   4        5
#      b        9  10       11
print(frame.swaplevel('key1', 'key2').sort_index(0))

# 许多对DataFrame和Series的描述和汇总统计都有一个level选项
# 用于指定在某条轴上求和的级别，这里按key2纬度进行求和操作
# state  Ohio     Colorado
# color Green Red    Green
# key2
# 1         6   8       10
# 2        12  14       16
print(frame.sum(level='key2'))
# 列操作也是同样道理
# color      Green  Red
# key1 key2
# a    1         2    1
#      2         8    4
# b    1        14    7
#      2        20   10
print(frame.sum(level='color', axis=1))
