# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 16:37
 @desc: 第518题

        给定不同面额的硬币和一个总金额。写出函数来计算可以凑成总金额的硬币组合数。假设每一种面额的硬币有无限个。
"""

"""
    解题思路：（完全背包问题，给定包的体积，每个物品有一个体积和价值，可以无限次取用，求包的最大价值）
        
        本题，给定总钱数amount，每个硬币的钱数，可以无限次取用，求拼凑成amount时的总方案数。
        
        状态表示：
            dp[i][j]：前i种硬币凑成总钱数为j的方案数
            
        状态转移：
            
            第i种硬币可以选0个，选1个，选2个，...，选k个，直至 (k+1) * coins[i] > j 为止
            
            我们用字母c表示coins[i]
            
            有：dp[i][j] = dp[i-1][j-0c]+dp[i-1][j-1c]+dp[i-1][j-2c]+...+dp[i-1][j-kc]
            
        此时时间复杂度为O(n^3)，两轮状态+1轮求和，可以进行优化
        
            根据上式，用j-c替代j，得：
                dp[i][j-c] = dp[i-1][j-1c]+dp[i-1][j-2c]+...+dp[i-1][j-kc], 这里j-(k+1)c越界，故不考虑
            
            故：dp[i][j] = dp[i-1][j] + dp[i][j-coins[i]]，这个方程可以优化成一维数组
            
        按照完全背包问题的思想，j从小往大，顺序遍历，遍历区间为 range(coins[i], amount+1)，
        
        dp[i-1][j] 就相当于上一轮的dp[j]，从小往大遍历，所以在第i轮的时候，dp[j-coins[i]]也已经进行了更新
        
              
        因此最终可得一维dp方程：dp[j] = dp[j] + dp[j-coins[i]]，即：dp[j] += dp[j-coins[i]]
"""


class Solution:
    def change(self, amount: int, coins):
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1  # 初始化dp[0]=1,表示总钱数为0时，拼凑方案为1
        for i in range(n):
            for j in range(coins[i], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i]]
        return dp[amount]
