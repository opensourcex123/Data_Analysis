# 作者：宁方笑
# 开发时间：2021/5/31 21:16
import pandas as pd

d=pd.Series([9,8,7,6],index=['a','b','c','d'])  #pandas库的强大之处在于可以自定义索引
print(d)
print(d[['a','b']]) #混合索引和自定义索引并存但不能一起使用
print('--------------')
a=pd.Series([1,2,3],['c','d','e'])
b=pd.Series([9,8,7,6],['a','b','c','d'])
print(a+b)  #Series的对齐操作，相同的索引进行加减