# 作者：宁方笑
# 开发时间：2021/5/29 21:32
import numpy as np
import matplotlib.pyplot as plt
#面向对象的方式绘制图形
fig,ax=plt.subplots()
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title('Simple Scatter')

plt.show()