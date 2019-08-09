# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/6 21:27
 @desc:
"""


class Solution:
    def getTranslationCount(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 计数问题，可以尝试动态规划法
        if not s:
            return -1
        dp = [1] * (len(s))  # 初始化为1,dp[0]=1，在计算dp[1]时，会用到dp[-1]，此时它的值为1
        for i in range(1, len(s)):
            dp[i] = dp[i - 1]
            if 10 <= int(s[i - 1:i + 1]) <= 25:
                dp[i] += dp[i - 2]
        return dp[-1]
