# encoding: utf-8
"""
 @project:剑指offer_by_Python
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/1/19 8:24 PM
 @desc: 在一个长度为n的数组里的所有数字都在0到n-1的范围内。 数组中某些数字是重复的，但不知道有几个数字是重复的,也不知道每个数字重复几次,
        请找出数组中任意一个重复的数字！
"""


class Solution:
    """
    解法思路： n个坑，n个数，找重复元素

    如果这个数组中没有重复的数字，那么数组排序之后，数字i必定会出现在下标为i的位置，

    所以遍历数组i,如果当前元素与index不相等，就交换两个元素，直至当前元素与index相等为止.
    """

    def duplicate(self, nums):
        if nums is None:
            return -1
        # 检查输入的数组是否在[0,n-1]区间内
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] > len(nums) - 1:
                return -1
        for i in range(len(nums)):
            while i != nums[i] and nums[i] != nums[nums[i]]:
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp  # 这里交换的时候，得按照这种方式，不能用 a, b = b, a
            if i != nums[i] and nums[nums[i]] == nums[i]:
                return nums[i]
        return -1


if __name__ == '__main__':
    sol = Solution()
    test_nums = [2, 3, 5, 4, 3, 2, 6, 7]
    print(sol.duplicate(test_nums))
