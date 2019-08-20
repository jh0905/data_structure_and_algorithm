# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/6/19 1:43 PM
 @desc:
"""
import time

import math


def f(m, n):
    if n == 0:
        return 1
    elif n == 1:
        return m
    elif m == n:
        return 1
    else:
        return f(m - 1, n - 1) + f(m - 1, n)


time1 = time.time()
a = f(5, 0)
time2 = time.time()
print("耗时：{}秒".format(time2 - time1))

print(a)


def g(m, n):
    if n == 0:
        return 1
    if n > m // 2:
        n = m - n
    sum_1 = sum_2 = 0
    for i in range(n + 1, m + 1):
        sum_1 += math.log(i)
    for j in range(1, m - n + 1):
        sum_2 += math.log(j)
    return math.exp(sum_1 - sum_2)


time1 = time.time()
b = round(g(5, 0))
time2 = time.time()
print("耗时：{}秒".format(time2 - time1))
print(b)
