# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 17:45
# 文件名称: hw_003_判断周期函数1.py
# 开发工具: PyCharm
# y=cos4 是否为周期函数
import numpy as np
import matplotlib.pyplot as plt

X = [4 * x for x in np.arange(100)]
Y = np.cos(X)

plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签
plt.plot(X, Y)
plt.show()
"""
常用求周期函数的方法:
1.找到一个T!=0,使得f(x+T)=f(x)
2.利用周期函数的性质证明

"""
