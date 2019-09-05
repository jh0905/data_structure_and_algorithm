# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 09:47
 @desc: 第53题
"""


class Solution:
    def maxSubArray(self, nums):
        n = len(nums)
        dp = [nums[0]] * n
        ans = dp[0]
        for i in range(1, n):
            dp[i] = max(0, dp[i - 1]) + nums[i]
            ans = max(dp[i], ans)
        return ans
