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


# log N的时间复杂度很低，我们直接设置搜索区间为[0,10010]
l = 0
r = 10010
while l < r:
    mid = (l + r) // 2
    # 如果mid成立，那么说明答案在左区间，用模板1（见下文）
    if check(mid):
        r = mid
    else:
        l = mid + 1
print(l)
