# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/7/19 7:36 PM
 @desc:
"""
N = int(input())
h = [int(x) for x in input().strip().split()]


# 判断能量值e能否跳完所有建筑
def check(e):
    for i in range(N):
        e = 2 * e - h[i]
        if e < 0:
            return 0
    return 1


l = min(h)
r = max(h) + 1
while l < r:
    mid = (l + r) // 2
    # 如果mid不成立，那么说明答案在右区间
    if not check(mid):
        l = mid + 1
    else:
        r = mid
        res = mid
print(res)
