# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 10:50
 @desc: 第153题
"""


class Solution:
    def findMin(self, nums):
        l = 0
        r = len(nums) - 1
        if nums[r] > nums[0]:  # 未发生旋转的情况
            return nums[0]
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

    def findMin2(self, nums):
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] <= nums[-1]:  # 右边数组中的数字都小于或等于队尾元素
                r = mid
            else:
                l = mid + 1
        return nums[r]


if __name__ == '__main__':
    print(Solution().findMin([2, 1]))
    print(Solution().findMin([1, 2]))
    print(Solution().findMin2([2, 1]))
    print(Solution().findMin2([1, 2]))
