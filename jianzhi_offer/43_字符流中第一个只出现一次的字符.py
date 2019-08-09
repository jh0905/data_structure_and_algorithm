# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 15:03
 @desc:
"""


class Solution:
    d = dict()
    queue = list()

    def firstAppearingOnce(self):
        """
        :rtype: str
        """
        if not self.queue:
            return "#"
        else:
            return self.queue[0]

    def insert(self, char):
        """
        :type char: str
        :rtype: void
        """
        if char in self.d.keys():
            self.d[char] += 1
        else:
            self.d[char] = 1
            self.queue.append(char)
        while self.queue and self.d[self.queue[0]] > 1:  # 队首元素必须为不重复的元素
            self.queue.pop(0)
