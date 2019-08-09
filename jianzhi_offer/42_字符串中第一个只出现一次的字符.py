# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 10:25
 @desc:
"""


class Solution:
    def firstNotRepeatingChar(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return '#'
        d = dict()
        for ch in s:
            if ch in d.keys():
                d[ch] += 1
            else:
                d[ch] = 1
        d = sorted(d.items(), key=lambda item: item[1])
        if d[0][1] == 1:
            return d[0][0]
        return '#'
