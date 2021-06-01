# 作者：宁方笑
# 开发时间：2021/6/1 21:44
import pandas as pd
import numpy as np

a=pd.DataFrame(np.arange(12).reshape(3,4))
b=pd.DataFrame(np.arange(12,0,-1).reshape(3,4))
print(a>b)  #比较运算不进行补齐，所以结构不一致的话，程序会报错
c=pd.Series(np.arange(4))
print(a>c)  #广播运算