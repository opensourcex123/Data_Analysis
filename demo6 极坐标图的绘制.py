# 作者：宁方笑
# 开发时间：2021/5/29 21:23
import numpy as np
import matplotlib.pyplot as plt

N=10
theta=np.linspace(0.0,2*np.pi,N,endpoint=False)
radii=10*np.random.rand(N)  #饼图的高度
width=np.pi/2*np.random.rand(N) #每块饼所占的面积

ax=plt.subplot(111,projection='polar')
bars=ax.bar(theta,radii,width=width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r/10.))
    bar.set_alpha(0.5)

plt.show()