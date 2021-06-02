# 作者：宁方笑
# 开发时间：2021/6/2 21:08
import pandas as pd
import numpy as np

b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','b','d'])
print(b.sort_index(axis=0,ascending=True))  #排列行，默认升序，根据索引排序
print('-----------------')
print(b.sort_values(by=2,axis=0,ascending=False))   #对横轴，第二列进行降序排序
print('-----------------')
print(b.sum())  #按0轴计算
print('-----------------')
print(b.describe().loc['max'])  #dataframe移除了ix属性，只能用loc属性代替