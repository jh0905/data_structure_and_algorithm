# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 15:27
 @desc:
"""


class Solution(object):
    def lastRemaining(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[1] = 0
        for i in range(1, n + 1):
            dp[i] = (dp[i - 1] + m) % i
        return dp[-1]

    def lastRemaining_2(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        if n == 1:
            return 0
        return (self.lastRemaining_2(n - 1, m) + m) % n


if __name__ == '__main__':
    print(Solution().lastRemaining_2(996, 20))
