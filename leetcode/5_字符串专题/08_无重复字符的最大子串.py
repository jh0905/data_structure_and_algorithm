# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 18:40
 @desc: 第3题
"""
"""
 解法一：
        一维动态规划法
        
        (1)状态表示： dp[i]以第i个字符结尾的无重复字符串的最大长度
        (2)状态转移: 
                如果第i个字符，在前i-1个字符中未出现过，那么dp[i]=dp[i-1]
                如果第i个字符上次出现的位置，到本次位置之间的距离大于dp[i-1]，说明重复字符无影响，dp[i]=dp[i-1]+1
                    如:abcdeba，此时i指向结尾的a，dp[i]=dp[i-1]+1
                    
                如果第i个字符上次出现的位置，到本次位置之间的距离小于等于dp[i-1]，那么dp[i]=distance
                    如： bcada ，distance = 4-2 = 2 < dp[3] = 4
                        abcda，distance = 4-0 = 4 == dp[3] = 4，对应的dp[4]均等于distance
                        
        (3)边界处理：第0个字符的时候，dp[0] = dp[0-1] + 1 = dp[-1] + 1，所以我们初始化的时候，dp数组全为0
        
        在这里，判断字符是否出现过，以及上次出现的位置，我们用哈希表存起来，在python中即用字典结构存储。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        dp = [0] * len(s)
        d = dict()  # 用来存某个字符最近一次出现的位置
        res = 1
        for i in range(len(s)):
            if s[i] not in d:  # 说明元素第一次出现
                dp[i] = dp[i - 1] + 1
            elif i - d[s[i]] > dp[i - 1]:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = i - d[s[i]]
            d[s[i]] = i  # 存下当前元素的下标
            res = max(res, dp[i])
        return res


"""
 解法二：
      双指针法
      
      我们先来看看暴力做法，再看如何把暴力做法优化成双指针法
      
      暴力做法：枚举字符串中的每一个字符i，令 j = i，如果j没有越界，并且j到i之间，无重复字符，则 j-=1，直到出现重复字符停止，此时
      以i结尾的最长无重复子串长度为 i - j
      
      我们用双指针来实现此过程，指针i往右先走，每走一步，将对应字符的哈希值加1，然后判断当前字符的哈希值是否大于1，是的话，则说明前面
      存在重复字符，那么我们就要把指针j移动到该重复字符的右边一个位置，在该重复字符前面的元素，也都无效了，参考暴力法的思想，重复字符
      前面的字符没有意义。
      
      在这个过程中，我们要通过字典结构，实现哈希表，可以发现，哈希表中的每一个value保证为1，一旦出现2，则进行删除，删到为2的value降为
      1为止，以上就是双指针法的思路。
      
"""


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i, j = 0, 0
        d = dict()
        res = 0
        while i < len(s):
            d[s[i]] = d.get(s[i], 0) + 1  # 字典中i的值加1
            while d[s[i]] > 1:  # 说明第i个元素在前i-1个元素中已存在
                d[s[j]] -= 1  # 把j指针右移，顺便把s[j]对应的值减1，实际上是置为0。
                j += 1
            res = max(res, i - j + 1)
            i += 1
        return res
