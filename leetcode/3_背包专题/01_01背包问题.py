# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 15:40
 @desc: acwing 第2题

        有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。（只能使用一次，所以称作01背包问题）

        第 i 件物品的体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。输出最大价值。
"""

"""
解题思路

    二维动态规划

        1. 状态表示：dp[i][j]:将前i件物品（可能只装其中的部分物品）装入容量为j的背包中的最大价值。（问题分解）

        2. 状态转移：***
            (1) 如果不装第i件物品，那么问题就转化为“前i-1件物品放入容量为j的背包中的最大价值”, dp[i][j] = dp[i-1][j]

            (2) 如果装第i件物品，那么问题就转化为“前i-1件物品放入剩下的容量为j-v[i]的背包中的最大价值”
                                                                                    dp[i][j]=dp[i-1][j-v[i]]+w[i]
            最终的dp[i][j]取两种情况中的较大值。

            综合一下：dp[i][j]=max{dp[i-1][j],f[i-1][j-v[i]]+w[i]}

        3. 边界处理：对于二维动态规划问题，我们增加一行和一列，使得理解起来更加方便
            显然，当i=0或者j=0时 dp[0][j]和dp[i][0]都为零

    因为我们的dp数组增加了一行和一列，所以初始化v和w时也要记得增加一个元素。

    对物品从1到n进行遍历，循环里面再对体积从0到V进行遍历，时间复杂度和空间复杂度为O(nm)

    在最后，返回最大的价值，即为dp[n][1],dp[n][2],...,dp[n][m]中的最大值
"""


class Solution:

    def max_value(self, n, m, v, w):
        # 可以画一个二维矩阵，模拟算法的过程，能够更加清晰的明白动态规划的过程
        # dp[i][j]状态的重点在于，j的值一定要满足，但是前i个物品不一定会全部装入包中
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(m + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= v[i]:
                    dp[i][j] = max(dp[i][j], dp[i - 1][j - v[i]] + w[i])
        return dp[n][m]  # 最大值为前n件物品，总容量为m时的状态值。


if __name__ == '__main__':
    import sys

    n, m = map(int, input().split())  # n表示物品个数，m表示最大体积
    v, w = [0], [0]
    lines = sys.stdin.readlines()
    for line in lines:
        line = list(map(int, line.split()))
        v.append(line[0])
        w.append(line[1])
    print(Solution().max_value(n, m, v, w))
