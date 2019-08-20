# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 22:13
 @desc: acwing第4题
        有 N 种物品和一个容量是 V 的背包。

        第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。输出最大价值。
"""

"""
 解题思路：
    一个基本思路是，将此问题转换为01背包求解！
    
    比如物品1有3件，每件价值为2，我们不妨创建3个物品1，存在数组v和数组w中
    
    最终更新一下总物品数n即可，然后套用01背包问题进行求解。
"""


class Solution:
    def max_value(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, v[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[m]


if __name__ == '__main__':
    import sys

    n, m = map(int, input().split())
    lines = sys.stdin.readlines()
    v = [0]
    w = [0]
    n = 0
    for line in lines:
        line = list(map(int, line.split()))
        v.extend([line[0]] * line[2])
        w.extend([line[1]] * line[2])
        n += line[2]
    print(Solution().max_value(n, m, v, w))
