# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 09:30
 @desc: 第151题
"""

"""
 解题思路：
    本题实际上在剑指offer中也遇到过，只是本题的情况稍微复杂一点，存在多个空格。
    
    记录本题的目的在于，实现python自带的split()函数，主要涉及到的就是 数组/字符串 分段操作，为经典模板代码。
    
    其实也可以直接把切割好的有效字符串，添加到一个list中，再把list拼接成字符串，可是我只想进行字符串操作，不想使用列表。
    
    所以得到如下代码，看起来很长，但是里面用到的小技巧满多，可以作为之后的小积木使用。
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        while s and s[0] == ' ':  # 去除开头空格，要记得判断字符串不为空
            s = s[1:]
        while s and s[-1] == ' ':  # 去除末尾空格
            s = s[:-1]
        i = 0
        j = 0
        res = ''
        while i < len(s):
            while i < len(s) and s[i] == ' ':  # 分段模板代码，去空格
                i += 1
            if i > j:  # 说明i发生了移动，将多个空格转换成一个空格
                res += ' '
            j = i
            while j < len(s) and s[j] != ' ':  # 分段模板代码，找单词
                j += 1
            res += s[i:j][::-1]
            i = j
        return res[::-1]  # 整体翻转


if __name__ == '__main__':
    print(Solution().reverseWords("  hello world!  "))
