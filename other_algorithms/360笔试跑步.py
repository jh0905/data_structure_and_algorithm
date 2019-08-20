# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/14 11:05
 @desc:
"""


class Solution:
    def get_xy(self, l, r):
        # 两个点关于x轴对称
        import math
        c = 2 * math.pi * r
        while l > c:
            l -= c
        angle = l / c * 2 * math.pi
        x = round(r * math.cos(angle), 3)
        y = round(r * math.sin(angle), 3)
        return [[x, -y], [x, y]]


if __name__ == '__main__':
    l, r = [int(x) for x in input().strip('\n').split()]
    res = Solution().get_xy(l, r)
    print('{} {}'.format(res[0][0], res[0][1]))
    print('{} {}'.format(res[1][0], res[1][1]))
