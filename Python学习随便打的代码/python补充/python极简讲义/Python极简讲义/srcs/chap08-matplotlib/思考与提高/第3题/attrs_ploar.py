#!/usr/bin/env python
# coding=utf-8
import numpy as np 
import matplotlib.pyplot as plt

plt.style.use('seaborn')
#显示中文
plt.rcParams[u'font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False 

#设置属性标签
attr_labels = ['武力','政治','智力','统帅','魅力']
#标签大小
attr_size = len(attr_labels)
#武将及相应的属性值
player = {
    '诸葛亮':[38,95,100,92,92],
    '曹操':[72,94,91,96,96],
    '刘备':[75,78,74,73,99],
    '黄盖':[83,65,65,79,81]
}

#创建4个子图，这里选择极坐标图
plt.figure(figsize=(20,10))
ax1 = plt.subplot(221,projection='polar')
ax2 = plt.subplot(222,projection='polar')
ax3 = plt.subplot(223,projection='polar')
ax4 = plt.subplot(224,projection='polar')

#角度，因为有5个属性所以角度应该分为6个，最后一个与第一个重合
theta = np.linspace(0,2*np.pi,attr_size,endpoint=False)
theta = np.append(theta,theta[0])
for x in player:
    player[x] = np.append(player[x],player[x][0])

#绘制诸葛亮能力图
ax1.plot(theta,player['诸葛亮'],'c')
ax1.fill(theta,player['诸葛亮'],'c',alpha=0.3)#fill()填充颜色
ax1.set_xticks(theta)
ax1.set_xticklabels(attr_labels,y=0.01,fontsize=15)
ax1.set_title('诸葛亮',color='c',fontsize=20)
ax1.set_yticks([])
ax1.grid(False)
for a,b in zip(theta,player['诸葛亮']):
    ax1.text(a,b,b,fontsize=10)


ax2.plot(theta,player['曹操'],'m')
ax2.fill(theta,player['曹操'],'m',alpha=0.3)
ax2.set_xticks(theta)
ax2.set_xticklabels(attr_labels,y=0.01,fontsize=15)
ax2.set_title('曹操',color='m',fontsize=20)
ax2.set_yticks([])
ax2.grid(False)
for a,b in zip(theta,player['曹操']):
     ax2.text(a,b,b,fontsize=10)

ax3.plot(theta,player['刘备'],'r')
ax3.fill(theta,player['刘备'],'r',alpha=0.3)
ax3.set_xticks(theta)
ax3.set_xticklabels(attr_labels,y=0.01,fontsize=15)
ax3.set_title('刘备',color='r',fontsize=20)
ax3.set_yticks([])
ax3.grid(False)
for a,b in zip(theta,player['刘备']):
    ax3.text(a,b,b,ha='center',fontsize=10)

ax4.plot(theta,player['黄盖'],'y')
ax4.fill(theta,player['黄盖'],'y',alpha=0.3)
ax4.set_xticks(theta)
ax4.set_xticklabels(attr_labels,y=0.01,fontsize=15)
ax4.set_title('黄盖',color='y',fontsize=20)
ax4.set_yticks([])
ax4.grid(False)
for a,b in zip(theta,player['黄盖']):
     ax4.text(a,b,b,ha='center',fontsize=10)

plt.tight_layout()
plt.savefig('4.png')
plt.show()
