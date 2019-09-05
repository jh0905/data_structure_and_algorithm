# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 15:42
 @desc: 第300题
"""

"""
    状态表示：dp[i]表示以第i个元素结尾第上升序列的最大值
    状态转移：从第0到第i-1个元素进行遍历，如果num[j] < nums[i]，dp[i] = max(dp[i],dp[j] + 1)
"""


class Solution:
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        ans = 1
        for i in range(1, n):
            for j in range(0, i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
            ans = max(dp[i], ans)
        return ans
