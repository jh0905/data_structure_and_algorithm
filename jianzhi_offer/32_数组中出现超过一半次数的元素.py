# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 17:01
 @desc:
"""


class Solution(object):
    def moreThanHalfNum_Solution(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if count == 0:
                res = nums[i]
                count += 1
                continue
            if nums[i] == res:
                count += 1
            if nums[i] != res:
                count -= 1
        return res
