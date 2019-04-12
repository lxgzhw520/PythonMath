# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 17:27
# 文件名称: hw_002_绝对值函数的图像.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签

# 绝对值函数一般有两种表示方法
"""
y=-x   x<0
y=x    x>0
"""
# 所以 需要画两条线
# 取 [-1000,0] 画 y=-x
# 取 [0,1000] 画 y=x

X1 = np.arange(-1000, 0)
X2 = np.arange(0, 1000)
Y1 = [-i for i in X1]
Y2 = [i for i in X2]

# 画图
plt.plot(X1, Y1)
plt.plot(X2, Y2)
plt.title("绝对值函数")
plt.savefig("绝对值函数的图像.png")
plt.show()
