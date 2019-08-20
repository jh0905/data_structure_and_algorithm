# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/14 09:00
 @desc: 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
        如果有多对数字的和等于S，输出两个数的乘积最小的。
"""


# -*- coding:utf-8 -*-
class Solution:
    def FindNumbersWithSum(self, nums, s):
        if not nums:
            return []
        n = len(nums)
        i = 0
        j = n - 1
        min_v = float('inf')
        ans = []
        while i < j:
            sum = nums[i] + nums[j]
            if sum < s:
                i += 1
            elif sum > s:
                j -= 1
            else:
                product = nums[i] * nums[j]
                if product < min_v:
                    ans = [nums[i], nums[j]]
                    min_v = product
                i += 1
                j -= 1
        return ans


if __name__ == '__main__':
    print(Solution().FindNumbersWithSum([1, 2, 4, 7, 11, 15], 15))
