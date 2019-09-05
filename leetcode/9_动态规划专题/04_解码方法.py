# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 14:45
 @desc: 第91题
        一条包含字母 A-Z 的消息通过以下方式进行了编码：
                        'A' -> 1
                        'B' -> 2
                        ...
                        'Z' -> 26
        给定一个只包含数字的非空字符串，请计算解码方法的总数。
"""

"""
    解题思路：
        状态表示：dp[i]表示以前i个元素的编码方式
        状态转移：以第i个数字，单独表示一个字符，则 dp[i]+=dp[i-1]  ，s[i] != 0
                第i-1,i个元素组成的两个数字，表示一个字符，则 dp[i] += dp[i-2]  10<=s[i]<=26
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # 设置边界，表示前0个元素的编码方式，只有一种，空字符串
        for i in range(1, n + 1):
            if s[i - 1] != '0':  # 字符串的下标，从0开始，所以相应减1
                dp[i] += dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2:i]) <= 26:
                dp[i] += dp[i - 2]
        return dp[-1]
