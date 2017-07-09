# -*- coding:utf-8 -*-


# 下面为二项分布的数字特征示例，请完成以下练习：
# （1）仔细阅读，理解代码含义，并运行代码，看看结果如何？

# （1）此题为普通编程练习题
# （2）scipy.stats.binom(n,p)函数返回符合二项分布的离散随机变量rv,其独立试验次数为n，每次成功的概率为p
# （3）rv.mean()返回随机变量rv的均值
# （4）rv.var()返回随机变量rv的方差值
# （5）rv.moment(n,*args,*kwds)返回随机变量的n阶距
# （6）rv.stats(moments='mvsk')返回随机变量rv的状态，moments的参数可为m(均值),v(方差值),s(偏度),k(峰度),默认为mv

from scipy.stats import binom


def nc_of_binom():
    rv = binom(10, 0.2)
    print (rv.mean())
    print (rv.var())
    print (rv.moment(1))
    print (rv.moment(2))
    print (rv.moment(3))
    print (rv.moment(4))
    print (rv.stats(moments='mvsk'))


# the code should not be changed
if __name__ == '__main__':
    nc_of_binom()
