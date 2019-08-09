# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/8 08:33
 @desc:
"""


class Solution:
    res = 1

    # 时间复杂度为O(n^2)
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
                elif nums[j] == nums[i]:
                    dp[i] = max(dp[i], dp[j])
            self.res = max(self.res, dp[i])
        return self.res


if __name__ == "__main__":
    numbers = [1, 3, 6, 7, 9, 4, 10, 5, 6]
    sol = Solution()
    sol.lengthOfLIS(numbers)
    print(sol.res)
