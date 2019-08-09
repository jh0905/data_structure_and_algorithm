# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/6 22:49
 @desc:
"""


class Solution:
    def longestSubstringWithoutDuplication(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)  # dp[i]表示以第i个元素结尾的不含重复字符的最大子串长度
        d = dict()  # 用来保存26个字母，上一次出现的位置
        res = 0
        for i in range(0, len(s)):
            if s[i] not in d.keys():  # 判断第i个元素在之前有没有出现过
                dp[i] = dp[i - 1] + 1
            else:
                distance = i - d[s[i]]
                if distance > dp[i - 1]:
                    dp[i] = dp[i - 1] + 1
                else:
                    dp[i] = distance
            d[s[i]] = i  # 更新第i个元素最后出现的位置
            res = max(res, dp[i])
        return res


if __name__ == "__main__":
    string = 'abcabc'
    print(Solution().longestSubstringWithoutDuplication(string))
