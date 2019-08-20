# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 15:24
 @desc: 第162题
"""


class Solution:
    def findPeakElement(self, nums):
        if not nums:
            return -1
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[mid + 1]:  # 每次可以判断左右两边必存在一个答案
                l = mid + 1
            else:
                r = mid
        return l
