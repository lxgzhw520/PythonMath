# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-12 17:12
# 文件名称: hw_001_正弦函数的图像.py
# 开发工具: PyCharm

# 导入依赖  numpy  pyplot
import numpy as np
from matplotlib import pyplot as plt

# 设置定义域和值域
plt.rcParams['font.family'] = ['Arial Unicode MS']  # 用来正常显示中文标签
# 设置图形大小
# plt.figure(figsize=(20, 8), dpi=80)
Df = np.linspace(-np.pi / 2, np.pi / 2, 1000)
Rf = np.sin(Df)

# 画图

plt.plot(Df, Rf, label='正弦函数')
plt.xlabel('定义域')
plt.ylabel('值域')
plt.title('正弦函数')
plt.grid()
plt.savefig("正弦函数的图像.png")
plt.show()
