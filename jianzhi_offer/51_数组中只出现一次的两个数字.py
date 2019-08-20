# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 20:50
 @desc:
"""


class Solution(object):
    def findNumsAppearOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        s = 0
        # 假设返回的是x,y，那么所有数字进行异或操作之后，只剩下x^y
        for num in nums:
            s ^= num
        k = 0
        while s >> k & 1 != 1:  # s的二进制表示中，从右往左第k个数为1
            k += 1
        x = 0
        for num in nums:
            if num >> k & 1 == 1:
                x ^= num
        return [x, s ^ x]



