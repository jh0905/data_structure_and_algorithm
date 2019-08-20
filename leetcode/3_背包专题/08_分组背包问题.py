# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 15:09
 @desc:
        有 N 组物品和一个容量是 V 的背包。

        每组物品有若干个，同一组内的物品最多只能选一个。

        每件物品的体积是 vij，价值是 wij，其中 i 是组号，j 是组内编号。

        求解将哪些物品装入背包，可使物品总体积不超过背包容量，且总价值最大。输出最大价值。
"""

"""
 解题思路：
 
    这道题实际上也是01背包问题的变种，我们同样是首先对组的总数进行遍历，然后再对体积从大到下遍历。
    
    在01背包问题中，我们直接是 dp[j] = max(dp[j],dp[j-v[i]]+w[i])
    
    在分组背包问题中，这一步变为：（k表示该组中有k件物品）
    
    dp[j]=max(dp[j],dp[j-v[1]]+w[1],dp[j-v[2]]+w[2],...,dp[j-v[k]]+w[k])，即再加一层循环，取每一组中的最大值。 
    
    另外，背包问题的解法，可以再简化一点，前面的学习中，我都是先把所有物品全部收集完毕，再进行动态规划，其实我们是可以在
    接收数据的同时，就开始动态规划的过程，详细代码如下：(前面的背包问题，也可以直接简化，在接收输入的同时执行动态规划)
"""

if __name__ == '__main__':
    n, m = map(int, input().split())
    dp = [0] * (m + 1)
    for i in range(1, n + 1):
        v, w = [0], [0]
        s = int(input())
        for _ in range(s):
            line = list(map(int, input().split()))
            v.append(line[0])
            w.append(line[1])
        for j in range(m, -1, -1):
            for k in range(1, s + 1):
                if j >= v[k]:
                    dp[j] = max(dp[j], dp[j - v[k]] + w[k])
    print(dp[m])
