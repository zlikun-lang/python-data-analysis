import sys

import pandas as pd
from pandas import DataFrame

# 某班级ABCD四次考试成绩数据
frame = DataFrame({
    '张三': [71, None, 82, 95],
    '李四': [87, 63, None, 48],
    '王五': [94, 76, 67, 62],
    '赵六': [81, 89, 78, None],
}, index=list('ABCD'))

print(frame)

## 写入CSV文件
# 将数据写入CSV文件（可能需要事先在当前目录下创建.data目录）
# frame.to_csv('.data/16.csv')
# 默认分隔符为英文逗号，可以通过sep参数自行指定
frame.to_csv('.data/16.csv', sep=',')
# 可以指定输出为当前控制台，当值为NA是，用NULL表示（默认以空白表示）
# ,张三,李四,王五,赵六
# A,71.0,87.0,94,81.0
# B,NULL,63.0,76,89.0
# C,82.0,NULL,67,78.0
# D,95.0,48.0,62,NULL
frame.to_csv(sys.stdout, sep=',', na_rep='NULL')
# 默认会输出行和列的标签，可以禁用
# 71.0,87.0,94,81.0
# ,63.0,76,89.0
# 82.0,,67,78.0
# 95.0,48.0,62,
frame.to_csv(sys.stdout, index=False, header=False)
# 也可以只写出一部分列，并按指定的列标签排序
# ,张三,王五
# A,71.0,94
# B,,76
# C,82.0,67
# D,95.0,62
frame.to_csv(sys.stdout, columns=['张三', '王五'])
# 只输出前两行
# ,张三,王五
# A,71.0,94
# B,,76
frame[:2].to_csv(sys.stdout, columns=['张三', '王五'])
# 如果要输出第1行和第3行怎么办？


## 读取CSV文件
# http://pandas.pydata.org/pandas-docs/stable/io.html
frame2 = pd.read_csv('.data/16.csv',
                     header=0,
                     index_col=0,
                     na_values=['NULL'])
#      张三    李四  王五    赵六
# A  71.0  87.0  94  81.0
# B   NaN  63.0  76  89.0
# C  82.0   NaN  67  78.0
# D  95.0  48.0  62   NaN
print(frame2)

# 如果只读取指定行
#      张三    李四  王五    赵六
# A  71.0  87.0  94  81.0
# B   NaN  63.0  76  89.0
print(pd.read_csv('.data/16.csv',
                  header=0,
                  index_col=0,
                  nrows=2))

# 如果要逐块读取文件，需要设置chunksize（行数）
# 返回的TextFileReader是可迭代的，每次最多迭代chunksize行
chunker = pd.read_csv('.data/16.csv',
                      header=0,
                      index_col=0,
                      chunksize=3)
# <pandas.io.parsers.TextFileReader object at 0x000001E8DB777438>
print(chunker)
# 0000000000000000
#      张三    李四  王五    赵六
# A  71.0  87.0  94  81.0
# B   NaN  63.0  76  89.0
# C  82.0   NaN  67  78.0
# 1111111111111111
#      张三    李四  王五  赵六
# D  95.0  48.0  62 NaN
# ----------------
for i, piece in enumerate(chunker):
    print(str(i) * 16)
    print(piece)
print('-' * 16)
