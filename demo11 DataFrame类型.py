# 作者：宁方笑
# 开发时间：2021/6/1 21:10
import pandas as pd
import numpy as np
#DATe Frame是二维的带标签的数组类型
d=pd.DataFrame(np.arange(10).reshape(2,5))  #创建dataframe类型
print(d)
print('-------------------')
dt={'one':pd.Series([1,2,3],index=['a','b','c']),
    'two':pd.Series([9,8,7,6],index=['a','b','c','d'])} #index是行索引，字典的键为列索引
d1=pd.DataFrame(dt)
print(d1)
print('--------------------')
d2=pd.DataFrame(dt,index=['b','c','d'],columns=['two','three']) #自动补齐
print(d2)