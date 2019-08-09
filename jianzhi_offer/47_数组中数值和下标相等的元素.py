# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 18:53
 @desc:
"""


class Solution(object):
    def getNumberSameAsIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] - mid < 0:
                l = mid + 1
            else:
                r = mid
        if nums[l] - l == 0:
            return l
        return -1
