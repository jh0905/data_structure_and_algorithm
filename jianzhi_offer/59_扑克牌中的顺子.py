# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 11:26
 @desc:
"""


class Solution(object):
    def isContinuous(self, numbers):
        """
        :type numbers: List[int]
        :rtype: bool
        """
        if not numbers:
            return False
        numbers.sort()
        k = 0
        while not numbers[k]:  # 找到第一个不为0的元素下标
            k += 1
        for i in range(k + 1, len(numbers)):
            if numbers[i] == numbers[i - 1]:  # 有序数组，重复元素必相邻
                return False
        return numbers[-1] - numbers[k] <= 4
