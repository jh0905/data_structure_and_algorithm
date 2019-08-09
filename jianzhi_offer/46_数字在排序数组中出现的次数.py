# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 18:23
 @desc:
"""


class Solution(object):
    def getNumberOfK(self, nums, k):
        """
        :type nums: list[int]
        :type k: int
        :rtype: int
        """
        if not nums or k not in nums:
            return 0
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < k:  # 我们要求的值，是第一个等于k的元素的下标
                l = mid + 1
            else:
                r = mid
        temp = l  # 把l的值存起来
        l, r = 0, len(nums) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] > k:  # 我们要求的值，是最后一个等于k的元素的下标
                r = mid - 1
            else:
                l = mid
        return l - temp + 1
