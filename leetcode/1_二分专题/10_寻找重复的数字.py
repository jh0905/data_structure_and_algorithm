# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 15:40
 @desc: 第287题，n+1个坑，n个数
"""


class Solution:
    # 数字取值为1~n，所以重复数字必在此区间内
    # 我们是对取值区间划分，而不是对下标区间划分！
    def findDuplicate(self, nums):
        l = 1
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if self.check(nums, l, mid):  # 是否存在重复元素
                r = mid
            else:
                l = mid + 1
        return l

    def check(self, nums, l, mid):
        count = 0
        for num in nums:
            if l <= num <= mid:
                count += 1
        if count > mid - l + 1:
            return True
        return False
