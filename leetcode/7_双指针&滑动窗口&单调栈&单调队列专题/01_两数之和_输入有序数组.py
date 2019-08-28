# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 09:45
 @desc: 第167题
"""

"""
    解题思路：
        双指针算法一般分为三步：
        (1) 思考问题的暴力解法，本题用O(n^2)的解法，遍历每一个pair，返回和为S的pair
        (2) 分析是否存在单调性，本题中，数组是一个有序数组，单调递增
        (3) 如何进行优化？定义首尾指针，如果当前和大于target，则需要把尾指针左移；如果当前和小于target，则需要把首指针右移。
"""


class Solution:
    def twoSum(self, nums, target):
        if not nums:
            return []
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target:
                j -= 1
            elif s < target:
                i += 1
            else:
                return [i + 1, j + 1]
        return []
