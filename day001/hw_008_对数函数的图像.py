# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 21:32
# 文件名称: hw_008_对数函数的图像.py
# 开发工具: PyCharm

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签

X = np.arange(1, 1000)
Y = np.log(X)
Y1 = np.log2(X)
Y2 = np.log10(X)
plt.plot(X, Y)
plt.plot(X, Y1)
plt.plot(X, Y2)
plt.grid()
plt.show()
