# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/1 15:02
 @desc:
"""


class Solution:
    def reorder_array(self, nums):
        i = 0
        j = len(nums) - 1
        while i <= j:
            while i <= j and nums[i] % 2 == 1:
                i += 1
            while i <= j and nums[j] % 2 == 0:
                j -= 1
            if i <= j:
                nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    array = [int(x) for x in input().split()]
    print(Solution().reorder_array(array))
