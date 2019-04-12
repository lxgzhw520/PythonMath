# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 21:28
# 文件名称: hw_007_幂函数的图像.py
# 开发工具: PyCharm

# y=x**3 的图像

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签

X = np.arange(100)
Y = [x ** 3 for x in X]

plt.plot(X, Y)
plt.grid()
plt.title("y=x**3")
plt.show()
