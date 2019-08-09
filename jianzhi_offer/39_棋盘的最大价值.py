# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/6 21:59
 @desc:
"""


class Solution(object):
    def getMaxValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)  # 棋盘的行数
        n = len(grid[0])  # 棋盘的列数

        dp = [[0] * n for _ in range(m)]  # 初始化为0
        for i in range(0, m):
            for j in range(0, n):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
        return dp[m - 1][n - 1]
