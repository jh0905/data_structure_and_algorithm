# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/6/19 3:18 PM
 @desc:
"""
n, m = [int(x) for x in input().split()]  # n为balls数组的长度,m为气球的颜色数
balls = [int(x) for x in input().split()]
i = j = 0  # i表示前指针，j表示后指针
colors = 0
color_list = [0] * (m + 1)  # 这里初始化为m+1，是为了保证编号为j的气球，对应color_list[j]，把color_list[0]空出来

res = n + 1  # 初始化返回值

while j < n:
    # 如果击中了气球并且滑动窗口中没这个值
    if balls[j] != 0 and color_list[balls[j]] == 0:
        colors += 1
    color_list[balls[j]] += 1
    if colors == m:  # 判断前指针的移动情况
        # balls[i] == 0 表示第i枪未命中气球,color_list[balls[i]] > 1表示有重复颜色气球被打破
        while balls[i] == 0 or color_list[balls[i]] > 1:
            color_list[balls[i]] -= 1
            i += 1
        res = min(res, j - i + 1)
    j += 1
print(res)
