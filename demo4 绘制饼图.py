# 作者：宁方笑
# 开发时间：2021/5/29 21:02
import matplotlib.pyplot as plt

labels='Frogs','Hogs','Dogs','Logs'
sizes=[15,30,45,10]
explode=[0,0.1,0,0]

#sizes:占格多少 explode：哪块突出 autopct：百分数显示格式 startangle：饼图起始角度
plt.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
plt.axis('equal')
plt.show()