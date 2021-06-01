# 作者：宁方笑
# 开发时间：2021/6/1 21:35
import numpy as np
import pandas as pd

a=pd.DataFrame(np.arange(12).reshape(3,4))
b=pd.DataFrame(np.arange(20).reshape(4,5))
print(a+b)  #补齐后进行运算
print(b.add(a,fill_value=100))  #将数据补齐100后进行运算
c=pd.Series(np.arange(4))
print(b-c)  #二维数据的每一行与以为数据进行广播运算