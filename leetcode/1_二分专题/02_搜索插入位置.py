# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 09:37
 @desc: 第35题
"""


class Solution:
    def searchInsert(self, nums, target):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] > target:  # 返回小于等于target的最后一个值
                r = mid - 1
            else:
                l = mid
        if nums[l] == target:
            return l
        elif nums[l] < target:
            return l + 1
        else:
            return 0

    def searchInsert2(self, nums, target):
        if not nums or target > nums[-1]:  # 排除边界情况
            return len(nums)
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] >= target:  # 返回小于等于target的最后一个值
                r = mid
            else:
                l = mid + 1
        return l


if __name__ == '__main__':
    print(Solution().searchInsert([1, 3, 5, 6], 7))
