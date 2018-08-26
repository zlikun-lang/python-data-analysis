import pandas as pd

data = {
    'id': ['Jack', 'Sarah', 'Mike'],
    'age': [18, 35, 21],
    'cash': [10.53, 500.7, 13.6]
}

# 创建一个数组框
df = pd.DataFrame(data)
#       id  age    cash
# 0   Jack   18   10.53
# 1  Sarah   35  500.70
# 2   Mike   21   13.60
print(df)
# <class 'pandas.core.frame.DataFrame'>
print(type(df))

# 高级参数，指定列名、索引名（行）
df = pd.DataFrame(data, columns=['id', 'age', 'cash'], index=['one', 'two', 'three'])
#           id  age    cash
# one     Jack   18   10.53
# two    Sarah   35  500.70
# three   Mike   21   13.60
print(df)

# 获取框中的数据
# one       Jack
# two      Sarah
# three     Mike
# Name: id, dtype: object
print(df['id'])

# 创建系列，系列是数据框的一个子集
s = pd.Series({'a': 4, 'b': 9, 'c': 16}, name='number')
# a     4
# b     9
# c    16
# Name: number, dtype: int64
print(s)

# 访问系列数据
# 4，按索引访问
print(s[0])
# 9，按键访问
print(s.b)
# a    4
# b    9
# Name: number, dtype: int64
print(s[:2])

# 还可以通过键增加一行
s['d'] = 25
# a     4
# b     9
# c    16
# d    25
# Name: number, dtype: int64
print(s)
