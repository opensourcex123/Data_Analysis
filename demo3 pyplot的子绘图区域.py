# 作者：宁方笑
# 开发时间：2021/5/28 21:06
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

a=np.arange(10)
gs=gridspec.GridSpec(3,3)

ax1=plt.subplot(gs[1,:2])
# ax2=plt.subplot(gs[0,0:2])  #注意还是左闭右开取键
plt.plot(a,2*a)
plt.show()
