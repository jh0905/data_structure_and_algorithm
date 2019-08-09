# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 21:37
 @desc:
"""


class Solution(object):
    def findNumberAppearingOnce(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = [0] * 32  # 统计每1个bit上，1出现的次数
        for num in nums:
            k = 0
            while k < 32:
                count[k] += num >> k & 1
                k += 1
        res = 0
        for i in range(32):
            # 因为其他数字都出现了三次，只有一个数字出现了一次
            # 也就说明count[i]%3等于0或1
            res += count[i] % 3 * 2 ** i
        return res

    def findNumberAppearingOnce_2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ones, twos = 0, 0
        for num in nums:
            ones = (ones ^ num) & ~ twos
            twos = (twos ^ num) & ~ ones
        return ones
