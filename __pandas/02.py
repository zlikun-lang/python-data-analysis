import pandas as pd

df = pd.DataFrame({
    'id': ['Jack', 'Sarah', 'Mike'],
    'age': [18, 35, 21],
    'cash': [10.53, 500.7, 13.6]
})

#       id  age    cash
# 0   Jack   18   10.53
# 1  Sarah   35  500.70
# 2   Mike   21   13.60
print(df)

# 成NumPy类似，支持向量化操作
# 0    False
# 1     True
# 2    False
# Name: cash, dtype: bool
print(df['cash'] > 100)
#       id  age   cash
# 1  Sarah   35  500.7
print(df[df['cash'] > 100])

