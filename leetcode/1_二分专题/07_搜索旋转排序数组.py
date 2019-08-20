# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 14:52
 @desc: 第33题

        假设按照升序排序的数组在预先未知的某个点上进行了旋转。

        ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

        搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

        你可以假设数组中不存在重复的元素。

        你的算法时间复杂度必须是 O(log n) 级别
"""


class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        # 找到最小元素
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid + 1
        # 设定二分搜索区间
        if target <= nums[-1]:
            r = len(nums) - 1
        else:
            l = 0
            r -= 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if target == nums[l]:  # 这里建议用l，因为可能存在r=-1，所以用l更稳妥
            return l
        return -1
