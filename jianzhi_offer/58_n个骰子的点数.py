# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 08:44
 @desc:
"""


class Solution(object):
    def numberOfDice_2(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return 0
        res = []
        for i in range(n, 6 * n + 1):
            res.append(self.dfs(i, n))
        return res

    # 递归两个要素：1.递归表示 2.递推公式 ，自上而下的顺序
    def dfs(self, s, n):
        if n < 1 or s <= 0:
            return 0
        if n == 1 and 0 < s < 7:
            return 1
        res = 0
        for i in range(1, 7):
            res += self.dfs(s - i, n - 1)
        return res

    def numberOfDice(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if not n:
            return 0
        dp = [[0] * (6 * n + 1) for _ in range(0, n + 1)]  # 创建一个(n+1)* 6n 的二维矩阵
        for i in range(1, 7):  # 边界处理，1个骰子和的取值为1,2,3,4,5,6的情况数全为1
            dp[1][i] = 1
        for i in range(2, n + 1):  # 枚举骰子个数，从2开始
            for j in range(i, 6 * i + 1):  # 枚举i个骰子和的取值
                for k in range(1, 7):  # i个骰子和为j的总情况数，等于i-1个骰子和为j-1,j-2,...总情况数之和
                    dp[i][j] += dp[i - 1][j - k]
        return dp[-1][n:]  # 最后一层，从第n个元素开始，即为所求


if __name__ == '__main__':
    print(Solution().numberOfDice(2))
