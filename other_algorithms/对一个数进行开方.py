# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 23:12
 @desc:
"""


class Solution:
    def sqrt(self, num):
        p = num
        q = num / 2
        while abs(p - q) > 0.00001:
            p = q
            q = (p + num / p) / 2
        return p


if __name__ == "__main__":
    sol = Solution()
    print(round(sol.sqrt(4), 3))
