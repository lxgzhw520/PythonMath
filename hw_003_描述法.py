# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-25 20:23
# 文件名称: hw_003_描述法.py
# 开发工具: PyCharm

"""
任何一个奇数都可以表示为 x=2k+1的形式:
    2k一定是偶数
    偶数+1 一定是奇数
"""
import math

print(math.sqrt(2))

"""
分别用列举法和描述法表示下列集合
    1 方程x**2-2=0的所有实数根的集合
    2 由大于10小于20的所有整数组成的集合
"""

# 列举法
example01 = {-math.sqrt(2), math.sqrt(2)}
print(example01)

# 集合推导式能直接用
example02 = {i for i in range(11, 20)}
print(example02)

#描述法
"""
in 表示属于
1 D={x in R | x**2=2}
2 D={x in N+ | 10<x<20}
"""
