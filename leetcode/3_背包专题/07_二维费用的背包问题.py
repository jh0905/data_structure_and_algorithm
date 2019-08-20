# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 12:52
 @desc: acwing第8题
        有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。

        每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。

        求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。输出最大价值。
"""

"""
 解题思路：
    本题是01背包问题的变种，在包体积的限制基础上，增加了一维重量的限制。
    
    于是我们需要把一维的dp数组，扩展到二维，dp[i][j]表示体积最大为i质量最大为j的背包中，最大物品价值是多少。
    
    我们在传统的01背包问题的基础上，枚举背包的体积时，再增加一层枚举质量的内层循环即可。
    
    即 dp[j][k] = max(dp[j][k],dp[j-v[i]][k-m[i]]+w[i])，i表示前i件商品。

"""


class Solution:
    def max_value(self, N, V, M, v, m, w):
        dp = [[0] * (M + 1) for _ in range(V + 1)]
        for i in range(1, N + 1):
            for j in range(V, v[i] - 1, -1):  # 对体积的枚举
                for k in range(M, m[i] - 1, -1):  # 对质量的枚举
                    dp[j][k] = max(dp[j][k], dp[j - v[i]][k - m[i]] + w[i])
        return dp[V][M]


if __name__ == '__main__':
    N, V, M = map(int, input().split())
    v, m, w = [0], [0], [0]
    import sys

    lines = sys.stdin.readlines()
    for line in lines:
        line = list(map(int, line.split()))
        v.append(line[0])
        m.append(line[1])
        w.append(line[2])
    print(Solution().max_value(N, V, M, v, m, w))

# 同样可以简化代码，在输入时进行判断

# if __name__ == '__main__':
#     N, V, M = map(int, input().split())
#     dp = [[0] * (M + 1) for _ in range(V + 1)]
#     for i in range(1, N + 1):
#         v, m, w = map(int, input().split())
#         for j in range(V, v - 1, -1):
#             for k in range(M, m - 1, -1):
#                 dp[j][k] = max(dp[j][k], dp[j - v][k - m] + w)
#     print(dp[V][M])
