# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 19:35
 @desc: 第664题
        有台奇怪的打印机有以下两个特殊要求：

        打印机每次只能打印同一个字符序列。
        每次可以在任意起始和结束位置打印新字符，并且会覆盖掉原来已有的字符。
        给定一个只包含小写英文字母的字符串，你的任务是计算这个打印机打印它需要的最少次数。

    示例：
        输入: "aba"
        输出: 2
        解释: 首先打印 "aaa" 然后在第二个位置打印 "b" 覆盖掉原来的字符 'a'。
"""

"""
    解题思路：区间DP问题
    
    状态表示：dp[l][r]表示打印机把下标为l到下标为r这一段字符串打印正确所需要的最少次数。
    
    状态转移：从最左侧开始，打印到某一个为止，可以将[l,r]划分成一系列的区间
            dp[l,l] + dp[l+1,r]
            dp[l,l+1] + dp[l+2,r]
            dp[l,l+2] + dp[l+3,r]
                     ...
            dp[l,r-2] + dp[r-1,r]
            dp[l,r-1] + dp[r,r]
            dp[l,r]
            
            计算每一种方案的最小值，作为dp[l][r]的值
            
    具体讨论：
            (1)如果第一次只打印第l个元素，需要1次，此时dp[l][r] = dp[l+1][r] + 1
            
            (2)如果第一次从l打印到第k个元素，注意，需要满足s[l]==s[k]，否则的话，说明第k个元素还需要进行一次打印，
                那就说明dp[l][k]不是最少次数了，所以从l到k打印成同一个字符时，必须满足第l个字符和第k个字符相等。
                
               这一部分的操作次数为dp[l][k-1]，因为第k个元素和第l个元素相等，我们打印l到k-1时，顺带把第k个元素也打印
               另一部分，第k+1个元素打印到第r个元素，即 dp[k+1][r]
            因此 dp[l][r] = dp[l][k-1] + dp[k+1][r]
"""


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        for interval in range(1, n + 1):  # 我们枚举l到r的区间长度，因为每一轮dp只会用到比它小的区间
            for l in range(n + 1 - interval):  # l的取值为n,n-1,n-2,...,3,2,1
                r = l + interval - 1  # l - r + 1 = interval,r是每一段区间长度的终点
                dp[l][r] = dp[l + 1][r] + 1  # 情况一：只打印左断点
                for k in range(l + 1, r + 1):  # 情况二：枚举从左端点打印到l+1,l+2,...r的所有情况
                    if s[k] == s[l]:
                        dp[l][r] = min(dp[l][r], dp[l][k - 1] + dp[k + 1][r])
        return dp[0][n - 1]  # 从第0个字符，打印到第n-1个字符，所需的最少次数
