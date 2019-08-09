# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/6 20:30
 @desc:
"""


class Solution(object):
    def printMinNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        if not nums:
            return ''
        nums = [str(x) for x in nums]
        from functools import cmp_to_key
        nums = sorted(nums, key=cmp_to_key(lambda x, y: int(x + y) - int(y + x)))
        return ''.join(nums).lstrip('0') or '0'  # 去除输入中可能存在的0，如果只有'0'，则返回'0'


if __name__ == '__main__':
    print(Solution().printMinNumber([0, 12]))
