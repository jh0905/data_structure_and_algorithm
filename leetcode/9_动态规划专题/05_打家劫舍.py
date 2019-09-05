# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 15:22
 @desc: 第198题
        你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是
        相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

        给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
"""
"""
    解题思路：【使用两个dp数组】
    
    状态表示：
        f[i]表示从前i个数中选，不选择第i个元素时的最大值
        g[i]表示从前i个数中选， 选择第i个元素时的最大值
    
    状态转移：
        f[i] = max(f[i-1],g[i-1])
        g[i] = f[i-1]+nums[i] 当前数选了，则上一个数不能选，不能从g[i-1]转移过来
"""


class Solution:
    def rob(self, nums):
        n = len(nums)
        f, g = [0] * (n + 1), [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = max(f[i - 1], g[i - 1])
            g[i] = f[i - 1] + nums[i - 1]  # 我们这里表示的是前i个元素，对应的nums数组，是第i-1个元素
        return max(f[n], g[n])
