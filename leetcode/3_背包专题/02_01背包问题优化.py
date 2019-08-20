# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 16:51
 @desc: 题目要求同上
        在上一讲中，时间复杂度和空间复杂度均为O(nm)，时间复杂度没法优化，但空间复杂度可以优化到O(m)，用一维动态规划数组实现
"""

"""
    一维动态规划和二维动态规划的共同点，在于都是用到了两层循环，但是内循环，枚举包的体积j时，采取逆序的方式。
    
    旧：dp[i][j] = max(dp[i-1][j], dp[i-1][j-v[i]] + w[i])
    
    新：dp[j] = max(dp[j], dp[j - v[i]] + w[i])
    
    其实两种做法，实现的目标是一样的，只不过一维数组更省空间，下面具体说说，为什么可以用一维数组来代替。
    
    举个例子，i = 3, j = 8, v[3] = 5, w[3] = 1
    
    旧：dp[3][8] = max(dp[2][8], dp[2][3] + w[3])   此时的dp[2][8]和dp[2][3]都是上一轮的状态值
    
    新：dp[8] = max(dp[8], dp[3] + w[3])      我们要保证dp[8]和dp[3]都是上一轮的状态值
 
    按照逆序的顺序，一维dp数组的更新顺序为：dp[8], dp[7], dp[6], ... , dp[3]
    
    也就是说，在本轮更新的值，不会影响本轮中其他未更新的值！
    
    如果按照顺序进行更新，dp[3] = max(dp[3], dp[0] + w[0])，对dp[3]的状态进行了更新，那么在更新dp[8]时，用到的dp[3]
    就不是上一轮的状态了，不满足动态规划的要求。
"""


class Solution:
    def max_value(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, -1, -1):
                if j >= v[i]:
                    dp[j] = max(dp[j], dp[j - v[i]] + w[i])
                else:
                    break
        return dp[-1]

    # 上述代码可以进行简化
    def max_value2(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, v[i] - 1, -1):  # j从m从大到小遍历到v[i]
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[-1]  # dp[m]表示前n个物品，体积小于等于m时的最大值，所以直接返回dp[-1]即为所求


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
#         for j in range(m, v[i] - 1, -1):
#             dp[j] = max(dp[j], dp[j - v[i]] + w[i])
#     print(dp[m])

# 观察发现，v和w只在本轮中会用到，所以不需要存为数组形式

# if __name__ == '__main__':
#     n, m = map(int, input().split())
#     dp = [0] * (m + 1)
#     for i in range(1, n + 1):
#         v, w = map(int, input().split())
#         for j in range(m, v - 1, -1):
#             dp[j] = max(dp[j], dp[j - v] + w)
#     print(dp[m])
