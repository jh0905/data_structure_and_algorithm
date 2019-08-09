# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 16:05
 @desc:
"""


class Solution(object):
    # 暴力解法,时间复杂度为O(n^2)
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    res += 1
        return res

    def merge(self, nums, l, r):
        if l >= r:
            return 0
        mid = l + r >> 1
        # 左边的逆序对的个数 + 右边逆序对的个数
        res = self.merge(nums, l, mid) + self.merge(nums, mid + 1, r)
        i, j = l, mid + 1
        sorted_nums = []
        # 统计归并之前，左边元素与右边元素构成逆序对的个数
        while i <= mid and j <= r:
            if nums[i] <= nums[j]:
                sorted_nums.append(nums[i])
                i += 1
            else:
                sorted_nums.append(nums[j])
                # print('{} {}'.format(nums[i:mid+1],nums[j]))
                j += 1
                res += mid - i + 1  # 统计左边有多少个大于右边当前值的元素
        while i <= mid:
            sorted_nums.append(nums[i])
            i += 1
        while j <= r:
            sorted_nums.append(nums[j])
            j += 1
        nums[l:r + 1] = sorted_nums  # 把进行归并所对应的原数组部分，用有序数组替代
        return res

    # 二路归并，时间复杂度为O(nlogn)
    def inversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return self.merge(nums, 0, len(nums) - 1)
