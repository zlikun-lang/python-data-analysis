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

# 写入json文件
frame.to_json(r'.data/17.json')
# {"\u5f20\u4e09":{"A":71.0,"B":null,"C":82.0,"D":95.0},"\u674e\u56db":{"A":87.0,"B":63.0,"C":null,"D":48.0},"\u738b\u4e94":{"A":94,"B":76,"C":67,"D":62},"\u8d75\u516d":{"A":81.0,"B":89.0,"C":78.0,"D":null}}
frame.to_json(sys.stdout)

# 读取json文件
frame2 = pd.read_json(r'.data/17.json', encoding='utf-8')
# A  71.0  87.0  94  81.0
# B   NaN  63.0  76  89.0
# C  82.0   NaN  67  78.0
# D  95.0  48.0  62   NaN
print(frame2)

# 写入pkl文件（二进制序列化）
frame.to_pickle('.data/17.pkl')
# 读取pkl文件
frame2 = pd.read_pickle('.data/17.pkl')
print(frame2)
