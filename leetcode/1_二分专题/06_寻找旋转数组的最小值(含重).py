# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 12:41
 @desc: 第154题
"""


class Solution:
    def findMin(self, nums):
        while len(nums) > 2 and nums[-1] == nums[0]:  # 删除后半截中可能存在的重复元素,但是数组长度必须大于2
            nums.pop()
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] <= nums[-1]:
                r = mid
            else:
                l = mid + 1
        return nums[l]

    # 如果输入为[3,1,3]，按照上一题的解法，输出则为3，所以我们需要去掉旋转字符串尾部和首部重复的元素
    # 但记得要排除字符串长度不能等于1 ，因此此时首尾元素是同一个元素，必相等，会把nums变为空
