# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 09:12
 @desc: acwing第十二题

        可能存在多种最优的装包方案，输出字典序最小的那一种。
"""

"""
 解题思路：
    其实在上一道题中，已经探讨了背包问题如何输出具体方案，物品的编号是按照输入顺序进行排的，我们传统构建dp数组的时候，是从前往后
    推导状态的，所以最大价值，在dp[n][m]处取得，然后在逆序遍历i=n,n-1,n-2,...,1，推测取得最大价值时，物品是否在包中。
    
    毫无疑问，上面这种做法，输出的方案是字典序最大的，我们想要输出字典序最小的话，即要做到两点。
    
    1. 最大价值要在dp[1][m]处取得
    2. 从i=1,2,3,...,n 推测取得最大价值时，物品是否在背包中。
    
    为此，我们构建二维dp数组的时候，外层循环，遍历i的顺序，就要逆序开始，状态转移方程也就变成
    dp[i][j] = max(dp[i+1][j],dp[i+1][j-v[i]]+w[i])
    
    因为会取到i=n，此时i+1变为n+1，于是我们初始化数组长度时，需要初始化有n+2行。
    
    最终实现代码如下，和上面类似，只是细微地方改动。
"""


class Solution:
    def max_value(self, n, m, v, w):
        dp = [[0] * (m + 1) for _ in range(n + 2)]
        for i in range(n, 0, -1):
            for j in range(0, m + 1):
                dp[i][j] = dp[i + 1][j]
                if j >= v[i]:
                    dp[i][j] = max(dp[i][j], dp[i + 1][j - v[i]] + w[i])
        # 最终最大值在dp[1][m]处取得
        vol = m
        res = []
        for i in range(1, n + 1):
            if dp[i][vol] == dp[i + 1][vol - v[i]] + w[i]:
                res.append(str(i))
                vol -= v[i]
        return ' '.join(res)


if __name__ == '__main__':
    n, m = map(int, input().split())
    v, w = [0], [0]
    for i in range(1, n + 1):
        line = list(map(int, input().split()))
        v.append(line[0])
        w.append(line[1])
    print(Solution().max_value(n, m, v, w))
