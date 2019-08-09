# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 19:44
 @desc:
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = float('-inf')  # 初始化 res 为负无穷
        dp = [0] * len(nums)
        for i in range(len(nums)):
            if dp[i - 1] < 0:
                dp[i - 1] = 0
            dp[i] = dp[i - 1] + nums[i]
            res = max(dp[i], res)
        return res
