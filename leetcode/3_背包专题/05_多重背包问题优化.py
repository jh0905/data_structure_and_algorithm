# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 09:27
 @desc:
"""
"""
 解题思路：
    
    前面提到的多重背包问题的解法，是把多件物品，转换成多个单件物品，添加到v和w数组中。
    
    如10件物品A, 则插入十条记录到v和w数组中，实际上这一过程可以进行优化！
    
    我们可以把十件物品A分成若干份，这若干份必须可以组合成0～10以内的任何一个数字。
    
    做法是：1,2,4,...,2^(k-1),10-2^k+1
    
    即：10可以分为 1，2，4，3
    
    显然这四个数字，可以组合成0～10以内的任何一个数字，如 8 = 1 + 4 + 3
    
    这么做的好处，是把时间复杂度从O(nm)降为O(m log n)，剩下的继续用01背包问题的解法求解。
    
    
"""


class Solution:
    def max_value(self, n, m, v, w):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            for j in range(m, v[i] - 1, -1):
                dp[j] = max(dp[j], dp[j - v[i]] + w[i])
        return dp[-1]


if __name__ == '__main__':
    import sys

    n, m = map(int, input().split())
    lines = sys.stdin.readlines()
    v, w = [0], [0]
    n = 0
    for line in lines:
        line = list(map(int, line.split()))
        k = 1
        while k <= line[2]:  # 假设line[2]=13,k取1,2,4之后，line[2] = 6 < k = 8 退出循环
            v.append(k * line[0])
            w.append(k * line[1])
            line[2] -= k
            k *= 2
            n += 1  # 物品总数加1
        if line[2]:
            v.append(line[2] * line[0])
            w.append(line[2] * line[1])
            n += 1
    print(Solution().max_value(n, m, v, w))
