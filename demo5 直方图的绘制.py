# 作者：宁方笑
# 开发时间：2021/5/29 21:09
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)
mu,sigma=100,20
a=np.random.normal(mu,sigma,size=100)   #正态分布

#第二个参数是直方块的个数
plt.hist(a,20,density=True,histtype='stepfilled',facecolor='b',alpha=0.75)
plt.title('Histogram')

plt.show()