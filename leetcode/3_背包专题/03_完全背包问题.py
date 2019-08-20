# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 21:03
 @desc: acwing 第3题

        有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。（区别于01背包的地方，物品有无限件）

        第 i 种物品的体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
"""

"""
    实现代码和01背包问题只有略微的变换，把体积遍历顺序从逆序改为顺序！
    
    上一篇代码中，解释过，逆序是为了保证更新当前状态时，用到的状态是上一轮的状态，保证每个物品只有一次或零次
    
    在这里，因为每个物品可以取任意多次，所以不再强求用上一轮的状态，即本轮放过的物品，在后面还可以再放
    
    不妨按照思路，模拟一遍过程。
    
    首先dp数组初始化全为0：给定物品种类有4种，包最大体积为5
    v[1] = 1, w[1] = 2
    v[2] = 2, w[2] = 4
    v[3] = 3, w[3] = 4
    v[4] = 4, w[4] = 5
    
    i = 1 时： j从1到5
    dp[1] = max(dp[1],dp[0]+w[1]) = w[1] = 2 (用了一件物品1）
    dp[2] = max(dp[2],dp[1]+w[1]) = w[1] + w[1] = 4（用了两件物品1）
    dp[3] = max(dp[3],dp[2]+w[1]) = w[1] + w[1] + w[1] = 6（用了三件物品1）
    dp[4] = max(dp[4],dp[3]+w[1]) = w[1] + w[1] + w[1] + w[1] = 8（用了四件物品1）
    dp[5] = max(dp[3],dp[2]+w[1]) = w[1] + w[1] + w[1] + w[1] + w[1] = 10（用了五件物品）
    
    i = 2 时：j从2到5
    dp[2] = max(dp[2],dp[0]+w[2]) = w[1] + w[1] = w[2] =  4（用了两件物品1或者一件物品2）
    dp[3] = max(dp[3],dp[1]+w[2]) = 3 * w[1] = w[1] + w[2] =  6（用了三件物品1，或者一件物品1和一件物品2）
    dp[4] = max(dp[4],dp[2]+w[2]) = 4 * w[1] = dp[2] + w[2] =  8（用了四件物品1或者，两件物品1和一件物品2或两件物品2）
    dp[5] = max(dp[5],dp[3]+w[2]) = 5 * w[1] = dp[3] + w[2] =  10（用了五件物品1或者，三件物品1和一件物品2或一件物品1和两件物品2）
 
    i = 3时：j从3到5
    dp[3] = max(dp[3],dp[0]+w[3]) = dp[3] = 6 # 保持第二轮的状态 
    dp[4] = max(dp[4],dp[1]+w[3]) = dp[4] = 8 # 保持第二轮的状态 
    dp[5] = max(dp[5],dp[2]+w[3]) = dp[4] = 10 # 保持第二轮的状态 
    
    i = 4时：j从4到5
    dp[4] = max(dp[4],dp[0]+w[4]) = dp[4] = 10 # 保持第三轮的状态
    dp[5] = max(dp[5],dp[1]+w[4]) = dp[5] = 10 # 保持第三轮的状态
    
    上面模拟了完全背包的全部过程，也可以看出，最后一轮的dp[m]即为最终的返回结果。
"""


class Solution:
    def max_value(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(v[i], m + 1):  # 区别于01背包问题，顺序遍历
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[m]


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

# 在进行输入的同时，开始动态规划过程，代码如下：

# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     dp = [0] * (m + 1)
#     v, w = [0], [0]
#     for i in range(1, n + 1):
#         line = list(map(int, input().split()))
#         v.append(line[0])
#         w.append(line[1])
#         for j in range(v[i], m + 1):
#             dp[j] = max(dp[j], dp[j - v[i]] + w[i])
#     print(dp[m])

# 进一步化简，因为每轮用到的v[i]和w[i]只在本轮输入中用到，后面不会再使用，因此不需要存为数组的形式

# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     dp = [0] * (m + 1)
#     for i in range(1, n + 1):
#         v, w = map(int, input().split())
#         for j in range(v, m + 1):
#             dp[j] = max(dp[j], dp[j - v] + w)
#     print(dp[m])
