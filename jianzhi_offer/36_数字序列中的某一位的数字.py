# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/6 15:57
 @desc:
"""


class Solution(object):
    def digitAtIndex(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 10:  # 10以内的输入单独处理，便于后面实现
            return n
        pos = 10  # 用来确定第n个数字的区间
        i = 1  # 用来确定第n个数字的位数
        while n >= pos:
            last_pos = pos
            pos = pos + 9 * pow(10, i) * (i + 1)
            i += 1
        p = (n - last_pos) // i  # 向下取整，确定第p个i位数
        q = (n - last_pos) % i  # 第p个i位数的第q位元素，为返回结果
        num = pow(10, i - 1) + p
        return int(str(num)[q])
