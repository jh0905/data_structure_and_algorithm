# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 11:08
 @desc: 第63题
        一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

        机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

        现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？
"""

"""
    解题思路：
        对于一个二维数组M，假设现在在M[i][j]位置
        如果M[i][j]是障碍物，那么dp[i][j] = 0，表示不存在路径
        如果是左上角的元素，赋值dp[i][j] = 1
        如果M[i][j]不是障碍物，那么dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
"""


class Solution:
    def uniquePathsWithObstacles(self, M):
        rows, cols = len(M), len(M[0])
        dp = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if M[i][j]:  # 如果是障碍物，直接跳过
                    continue
                if not i and not j:  # 如果在左上角，赋值为1
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]
