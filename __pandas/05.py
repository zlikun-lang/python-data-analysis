from pandas import DataFrame

# 另一种常见数据形式为嵌套字典
data = {
    'Nevada': {
        2001: 2.4,
        2002: 2.9
    },
    'Ohio': {
        2000: 1.5,
        2001: 1.7,
        2002: 3.6
    }
}

# 外层字典键为列，内层为行索引
# 内层行索引会被合并，空则使用NaN填充
obj = DataFrame(data)

#       Nevada  Ohio
# 2000     NaN   1.5
# 2001     2.4   1.7
# 2002     2.9   3.6
print(obj)

# 可以对结果转置
#         2000  2001  2002
# Nevada   NaN   2.4   2.9
# Ohio     1.5   1.7   3.6
print(obj.T)

# 如果设置了DataFrame的index和columns的name属性，则这些信息也会被输出出来
obj.index.name = 'year'
obj.columns.name = 'state'
# state  Nevada  Ohio
# year
# 2000      NaN   1.5
# 2001      2.4   1.7
# 2002      2.9   3.6
print(obj)

# 以二维数组形式返回DataFrame中的数据
# [[nan 1.5]
#  [2.4 1.7]
#  [2.9 3.6]]
print(obj.values)

