# 作者：宁方笑
# 开发时间：2021/5/31 21:06
import pandas as pd

d=pd.Series(range(20))
print(d)
print('-----------')
print(d.cumsum())   #计算前n项和