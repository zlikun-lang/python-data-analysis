from pandas import DataFrame, Series

frame = DataFrame({
    'a': range(2000, 2007),
    'b': range(7, 0, -1),
    'c': ['one'] * 3 + ['two'] * 4,
    'd': [0, 1, 2, 0, 1, 2, 3]
})

#       a  b    c  d
# 0  2000  7  one  0
# 1  2001  6  one  1
# 2  2002  5  one  2
# 3  2003  4  two  0
# 4  2004  3  two  1
# 5  2005  2  two  2
# 6  2006  1  two  3
print(frame)

# set_index函数用于将一个或多个列转换为行索引，返回一个新的DataFrame
#           a  b
# c   d
# one 0  2000  7
#     1  2001  6
#     2  2002  5
# two 0  2003  4
#     1  2004  3
#     2  2005  2
#     3  2006  1
frame2 = frame.set_index(['c', 'd'])
print(frame2)

# 默认列转换为行索引后，会从列中删除，可以通过drop=False将其保留下来
#           a  b    c  d
# c   d
# one 0  2000  7  one  0
#     1  2001  6  one  1
#     2  2002  5  one  2
# two 0  2003  4  two  0
#     1  2004  3  two  1
#     2  2005  2  two  2
#     3  2006  1  two  3
print(frame.set_index(['c', 'd'], drop=False))

# reset_index方法与set_index刚好相反，用于将索引转移到列里面
#      c     a  b
# d
# 0  one  2000  7
# 1  one  2001  6
# 2  one  2002  5
# 0  two  2003  4
# 1  two  2004  3
# 2  two  2005  2
# 3  two  2006  1
print(frame2.reset_index(['c']))
#      c  d     a  b
# 0  one  0  2000  7
# 1  one  1  2001  6
# 2  one  2  2002  5
# 3  two  0  2003  4
# 4  two  1  2004  3
# 5  two  2  2005  2
# 6  two  3  2006  1
print(frame2.reset_index(['c', 'd']))
