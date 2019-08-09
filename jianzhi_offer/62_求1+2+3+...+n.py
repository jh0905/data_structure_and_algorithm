# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 17:21
 @desc:
"""


class Solution(object):
    def getSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = n
        res += n and self.getSum(n - 1)
        return res


if __name__ == '__main__':
    print(Solution().getSum(100))
