# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 10:11
 @desc: 第34题
"""


class Solution:
    def searchRange(self, nums, target):
        # 两段二分
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid
        if nums[l] != target:
            return [-1, -1]
        t = l
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r + 1 >> 1
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid
        return [t, l]


if __name__ == '__main__':
    print(Solution().searchRange([0, 0, 0, 1, 2, 3], 0))
