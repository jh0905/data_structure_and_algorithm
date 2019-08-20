# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 19:28
 @desc:
"""
"""
 解题思路：
 
    (1)dp数组的初始化方式进行改变：
        - dp[0] = 0, 表示包体积为0时最大价值也为0。
        - 其余元素初始化为负无穷，此时dp[j]表示：求背包内的物品体积恰好为j时的最大价值，便于我们统计方案数
        - 其余元素初始化为0，此时dp[j]表示：求背包容量体积最大为j时的最大价值
        
        举个例子，假设背包最大体积为5，对于第1个输入，v = 3, w = 4, 那么j只能取5,4,3，于是dp[5] = max(dp[5],dp[5-3]+4)，
        注意此时dp[5]和dp[2]都是负无穷,所以dp[5]的值还是负无穷。
        
        到什么时候dp的值才会更新呢，即j==v时，dp[j] = max(dp[j],dp[j-v]+w) = dp[0]+w
        
        随后也是类似的逻辑，要么就j==v，要么dp[j-v]不为负无穷，不为负无穷的前提就是存在若干个物品的
        体积恰好为j-v。
        
        所以赋值为负无穷时，保证背包内的物品体积恰好为j.
    
    (2)开辟一个新的数组g
        - g[0] = 1，表示包内所有物品体积为0的方案数，此时只有一种方案，即什么物品都不装
        - g[j] 表示 包内物品体积为j且取得最大价值时的方案数，它也是可以通过两部分状态转移而来
          如果体积为j时取得最大价值时不需要放当前物品，则 s += g[j];
          如果体积为j时取得最大价值时需要放置当前物品，则 s += g[j-v]
        - 最终：g[j] = s
    
    (3)最后，根据初始化的原因，最终最大价值不一定在dp[j]处取得，因此我们需要遍历一遍dp数组，求出最大价值。
    然后根据最大价值，找到此时对应的总方案数g[j]，把所有等于最大价值的总方案数累加起来即可。另外记得取模。
"""
if __name__ == '__main__':
    mod = 10 ** 9 + 7
    n, m = map(int, input().split())
    dp = [0] + [float('-inf')] * m
    g = [1] + [0] * m  # g(0)表示体积为0时的方案数，初始化为1，只有一种方案，全都不装
    for i in range(1, n + 1):
        v, w = map(int, input().split())
        for j in range(m, v - 1, -1):
            s = 0
            t = max(dp[j], dp[j - v] + w)
            if t == dp[j]:
                s += g[j]
            if t == dp[j - v] + w:
                s += g[j - v]
            s = s % mod if s >= mod else s
            dp[j] = t
            g[j] = s
    max_v = 0
    for i in range(1, m + 1):
        max_v = max(max_v, dp[i])
    res = 0
    for i in range(1, m + 1):
        if dp[i] == max_v:
            res += g[i]
        res = res % mod if res >= mod else res
    print(res)
