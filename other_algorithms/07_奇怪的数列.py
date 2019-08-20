# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/6/19 12:13 PM
 @desc:
"""
a = int(input())
while a:
    l, r = [int(x) for x in input().split()]  # 获取输入的区间范围
    n_groups = (r - l + 1) // 2  # 获取分组数
    reset = 0
    if l % 2 == 0:  # l为偶数，相邻元素和为-1
        res = -1 * n_groups
    else:
        res = n_groups
    if (r - l + 1) % 2 == 1:  # 区间为奇数，剩了一个数，这里的 r 记得判断是正数还是负数!!!!!!
        print(res + r * pow(-1, r))
    else:
        print(res)
    a -= 1
