# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 21:44
 @desc: 第10题

        给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
            '.' 匹配任意单个字符
            '*' 匹配零个或多个前面的那一个元素
        所谓匹配，是要涵盖整个字符串s的，而不是部分字符串。
"""

"""
    解题思路：
    
        状态表示：dp[i][j]表示s串的前i个字符和p串的前j个字符是否匹配，值为True或False
        
        状态转移：讨论p[j]的取值情况
            (1)如果 p[j] != '*'，那么dp[i][j] = dp[i-1][j-1] and (s[i]与p[j]是否匹配)
            (2)如果 p[j] == '*'，那么需要枚举'*'的取值情况，0, 1, 2, 3, ...
            dp[i][j] = dp[i][j-2]  (*取0)
                    or dp[i-1][j-2] and s[i]与p[j-1]是否匹配      (*取1)
                    or dp[i-2][j-2] and s[i-1:i+1]与p[j-1]*2匹配  (*取2)
                    ......
                    
            优化：当p[j] == '*'时：
            dp[i-1][j] = dp[i-1][j-2]
                      or dp[i-2][j-2] and s[i-1]与p[j-1]是否匹配
                      or dp[i-3][j-2] and s[i-2:i]与p[j-1]*2匹配
            发现：
            dp[i][j] = dp[i][j-2] or dp[i-1][j] and s[i]与p[j-1]是否匹配
        
        因此，算法复杂度从O(n^3)优化成O(n^2)
"""


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        dp = [[False] * (m + 1) for _ in range(n + 1)]  # 因为是前i个字符，前j个字符
        s, p = ' ' + s, ' ' + p  # 为了后面下标表示方便，在前面加上一个一个无意义的字符
        for i in range(n + 1):
            for j in range(m + 1):
                if not i and not j:
                    dp[i][j] = True
                else:
                    if j + 1 <= m and p[j + 1] == '*':  # 当前元素的下一个状态是*的话，那么它的状态和下一个元素状态绑定，本轮不更新
                        continue
                    if p[j] != '*':  # 情况一
                        if p[j] == '.' or p[j] == s[i]:
                            if i > 0 and j > 0:
                                dp[i][j] = dp[i - 1][j - 1]
                    else:  # 情况二
                        if j >= 2:  # 情况二的子情况1
                            dp[i][j] = dp[i][j - 2]
                        if i > 0 and j > 0:  # 情况二的子情况2
                            if p[j - 1] == '.' or s[i] == p[j - 1]:
                                if dp[i - 1][j]:
                                    dp[i][j] = True
        return dp[n][m]
