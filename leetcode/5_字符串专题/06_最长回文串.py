# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 16:41
 @desc: 第5题

        输入: "babad"
        输出: "bab"
        注意: "aba" 也是一个有效答案。
"""

"""
 解题思路：
    
    本题采用的暴力解法，思想比较简单，也能够AC通过，代码看起来还是很漂亮的。
    
    回文串有两种情况：
      
      第一种是长度为奇数，如 "abcba"，对于这种情况，我们枚举每个字符时，定义两个指针，初始时等于该字符，然后分别向左和向右移动一位
      每轮判断 while l >= 0 and r < len(s) and s[l] == s[r] 是否成立，最终循环结束时，最长的串为s[l+1,r]，左闭右开
      
      第二种是长度为偶数，如 "abba" ，对于这种情况，我们枚举每个字符的时候，定义两个指针，一个指向i，另外一个指向i+1，然后分别
      向左向右移动，每轮判断 while l >= 0 and r < len(s) and s[l] == s[r]是否成立，最长的串也是s[l+1,r]
      
      每次我们比较一下当前最长回文串和返回res保存的回文串的长度，选择更长的那个作为res.
      
      代码真的看起来很漂亮。
"""


class Solution:
    # 中心扩展法
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):  # 枚举每一个字符
            # 考虑回文串长度为奇数的情况
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            res = s[l + 1:r] if len(s[l + 1:r]) > len(res) else res
            # 考虑回文串长度为偶数的情况
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            res = s[l + 1:r] if len(s[l + 1:r]) > len(res) else res
        return res
