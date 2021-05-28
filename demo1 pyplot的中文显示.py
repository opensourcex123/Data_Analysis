# 作者：宁方笑
# 开发时间：2021/5/27 21:38
import numpy as np
import matplotlib.pyplot as plt


a=np.arange(0.0,5.0,0.02)
plt.xlabel('横轴：时间',fontproperties='kaiti',fontsize=20)
plt.ylabel('纵轴：振幅',fontproperties='kaiti',fontsize=20)
plt.plot(a,np.cos(2*np.pi*a),'r--')
plt.show()