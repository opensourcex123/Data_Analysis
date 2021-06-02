# 作者：宁方笑
# 开发时间：2021/6/2 21:29
import pandas as pd
import numpy as np

b=pd.DataFrame(np.arange(20).reshape(4,5),index=['c','a','d','b'])
print(b)
print('------------------------')
print(b.cumsum())   #每一列的累加和
print('------------------------')
print(b.rolling(2).sum())   #窗口计算，2是窗口的大小，无前列则补NaN