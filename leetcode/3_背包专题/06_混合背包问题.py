# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/20 10:52
 @desc: acwing第7题
        有 N 种物品和一个容量是 V 的背包。

        物品一共有三类：

        第一类物品只能用1次（-1表示）；
        第二类物品可以用无限次（0表示）；
        第三类物品最多只能用 si 次（正整数表示）；
        每种体积是 vi，价值是 wi。

        求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。输出最大价值。
"""

"""
 解题思路：
    本题的解法，实际上是对前面三个问题的综合，我们做两点改变。
    
    我们知道多重背包问题，可以转换为01背包问题，所以此题实际上只有两类情况。
    
    1.我们在进行动态规划的时候，判断物品属于01背包问题时，在遍历体积时，采取逆序方式；属于完全背包问题时，则采取顺序方式。
    
    2.因此我们在接受输入的时候，只有1件的物品直接存到things中，无穷件的物品也是直接存到things中，有限件物品，转成多个单件物品，
    并赋值为类型-1，逐个存入到things数组中，
"""


class Thing:
    def __init__(self, v, w, type):
        self.v = v
        self.w = w
        self.type = type


class Solution:
    def max_value(self, n, m, things):
        dp = [0] * (m + 1)
        for i in range(1, n + 1):
            if things[i].type == -1:
                for j in range(m, things[i].v - 1, -1):
                    dp[j] = max(dp[j], dp[j - things[i].v] + things[i].w)
            else:
                for j in range(things[i].v, m + 1):
                    dp[j] = max(dp[j], dp[j - things[i].v] + things[i].w)
        return dp[m]


if __name__ == '__main__':
    import sys

    n, m = map(int, input().split())
    lines = sys.stdin.readlines()
    things = [Thing(0, 0, 0)]
    n = 0
    for line in lines:
        line = list(map(int, line.split()))
        if line[2] == -1:  # 单件物品
            things.append(Thing(line[0], line[1], -1))
            n += 1
        elif line[2] == 0:  # 无限件物品
            things.append(Thing(line[0], line[1], -1))
            n += 1
        else:  # 有限件物品，转成多个单件物品
            k = 1
            while k <= line[2]:
                things.append(Thing(k * line[0], k * line[1], -1))
                line[2] -= k
                k *= 2
                n += 1
            if line[2]:
                things.append(Thing(line[2] * line[0], line[2] * line[1], -1))
                n += 1
    print(Solution().max_value(n, m, things))
