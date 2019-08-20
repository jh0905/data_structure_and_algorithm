# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 20:09
 @desc:
"""

"""
 我们要求具体方案情况，具体做法是在二维dp数组的基础上进行求解，我们以01背包问题为例：
 
 枚举完每一个状态值dp[i][j]之后，我们得到一个二维矩阵，可以通过逆向推理得到，在得到最大价值时，具体选择了哪些物品。
 
 因为最大值是在dp[n][m]处取得，所以我们逆序遍历物品数i=n,n-1,n-2,...,2,1，判断当前物品是否在取得最大价值时的包中。

 初始时，vol = m :
  
 当i=n时，我们判断 dp[n][vol] == dp[n-1][vol-v[i]] + w[i] 是否成立？
 
 如果成立的话，说明第i件商品在包中，并将vol的值减去v[i]，不成立的话，则说明在取得最大价值时，第i件商品不在包中
 
 不论成立与否，i -= 1，再进行判断第i-1件商品是否在包中，成立的话，vol再减去v[i]的值，一直递归循环下去，直至i=1或者vol=0
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
        res = []
        vol = m
        for i in range(n, 1, -1):
            if dp[i][vol] == dp[i - 1][vol - v[i]] + w[i]:
                vol -= v[i]
                res.append(i)
        return res[::-1]


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
