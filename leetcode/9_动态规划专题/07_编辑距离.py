# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 15:58
 @desc: 第72题
        给定两个单词 word1 和 word2，计算出将 word1 转换成 word2 所使用的最少操作数 。

        你可以对一个单词进行如下三种操作：

        插入一个字符
        删除一个字符
        替换一个字符
"""

"""
    解题思路：
        状态表示：dp[i][j] 将第一个字符串的前i个字符变成第二个字符串的前j个字符时的最小方案
        
        状态转移：（对word1有三种操作）
         
          最后一步为插入操作：插入的一定是第2个单词的第j个字母，插之前，第一个单词的前i个字母已经和第二个单词的前i-1个
                           字母匹配了，则dp[i][j] = dp[i][j-1] + 1
          最后一步为删除操作：删之前，第1个单词的前i-1个字母已经和第2个单词的前j个字母匹配了，则
                           dp[i][j] = dp[i-1][j] + 1
          最后一步为替换操作：
                如果word[i]和word[j]相等，说明不需要替换，dp[i][j] = dp[i-1][j-1]
                如果word[i]和word[j]不等，说明需要替换，则dp[i][j] = dp[i-1][j-1] + 1
          
          取三种操作的最小值
        
        边界处理： dp[0][j] = j，要插入j个元素
                 dp[i][0] = i，要删除i个元素
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]  # 前i个字符，所以初始化为n+1
        for i in range(n1 + 1):
            dp[i][0] = i
        for j in range(n2 + 1):
            dp[0][j] = j
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1,
                               dp[i - 1][j - 1] + (word1[i - 1] != word2[j - 1]))  # True表示1，False表示0
        return dp[n1][n2]
