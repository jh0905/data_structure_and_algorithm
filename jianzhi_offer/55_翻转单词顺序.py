# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/8 15:05
 @desc:
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = s[::-1]
        i = 0
        while i < len(s):
            # 字符串划分模板
            j = i
            while j < len(s) and s[j] != ' ':  # 模板
                j += 1
            s = s.replace(s[i:j], s[i:j][::-1])  # 将单词进行翻转，并覆盖原单词
            i = j + 1
        return s

    def reverseWords_2(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(s.split()[::-1])


if __name__ == '__main__':
    print(Solution().reverseWords("I am a student."))
