# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 16:59
 @desc:
"""


class Solution(object):
    def maxDiff(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        res = 0
        min_v = nums[0]
        for num in nums[1:]:  # 从第2个数字开始枚举
            res = max(num - min_v, res)
            min_v = min(num, min_v)
        return res
