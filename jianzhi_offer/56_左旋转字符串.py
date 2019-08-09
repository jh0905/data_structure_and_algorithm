# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/8 16:29
 @desc:
"""


class Solution(object):
    def leftRotateString(self, s, n):
        """
        :type s: str
        :type n: int
        :rtype: str
        """
        s = s.replace(s[:n], s[:n][::-1])
        s = s.replace(s[n:], s[n:][::-1])
        return s[::-1]
