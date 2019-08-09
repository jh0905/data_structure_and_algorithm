# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 22:22
 @desc:
"""


class Solution(object):
    def findNumbersWithSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for num in nums:
            if num in d.keys():
                return [target - num, num]
            else:
                d[target - num] = num
