from pandas import DataFrame

data = {
    'id': ['Jack', 'Sarah', 'Mike'],
    'age': [18, 35, 21],
    'cash': [10.53, 500.7, 13.6]
}

# 使用字典结构构造DataFrame
obj = DataFrame(data)

#       id  age    cash
# 0   Jack   18   10.53
# 1  Sarah   35  500.70
# 2   Mike   21   13.60
print(obj)

# 指定索引，指定列（不存在则能NaN填充）
obj = DataFrame(data, index=['a', 'b', 'c'], columns=['id', 'gender', 'age'])
#       id gender  age
# a   Jack    NaN   18
# b  Sarah    NaN   35
# c   Mike    NaN   21
print(obj)

# 每一列是一个Series
# a     Jack
# b    Sarah
# c     Mike
# Name: id, dtype: object
print(obj['id'])

# 不存在的列，可以进行赋值设置值
obj['gender'] = 1
#       id  gender  age
# a   Jack       1   18
# b  Sarah       1   35
# c   Mike       1   21
print(obj)

# 也可以是一个迭代器，但迭代次数必须与行数匹配，其本质为切片赋值
obj['gender'] = [1, 0, 1]
#       id  gender  age
# a   Jack       1   18
# b  Sarah       0   35
# c   Mike       1   21
print(obj)

# del关键字可以删除列
del obj['gender']
#       id  age
# a   Jack   18
# b  Sarah   35
# c   Mike   21
print(obj)
