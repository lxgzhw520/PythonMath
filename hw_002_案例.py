# _*_ coding:UTF-8 _*_
# 开发人员: 理想国真恵玩-张大鹏
# 开发团队: 理想国真恵玩
# 开发时间: 2019-04-25 20:02
# 文件名称: hw_002_案例.py
# 开发工具: PyCharm

"""
用列举法描述下列集合
    1 小于10的所有自然数组成的集合
    2 方程x**2=x的所有实数根组成的集合
    3 由1-20以内所有的质数组成的集合
"""

# 自然数包括 0  正整数,负整数
example01 = set([i for i in range(10)])
print(example01)

# 很多数学问题中,经常要考虑参数为0的情况
example02 = {0,1}
print(example02, type(example02))

# 质数,除了1和自己,不能被其他数整除的数
num_list = []


def isPreme(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(isPreme(6))
for i in range(1, 21):
    # 得到1-20 判断是否是素数
    if isPreme(i):
        num_list.append(i)

print(num_list)
example03 = set(num_list)
print(example03)
