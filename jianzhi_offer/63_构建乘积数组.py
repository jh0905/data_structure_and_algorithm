# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 20:30
 @desc:
"""


class Solution(object):
    def multiply(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return []
        B = [1] * len(A)
        temp = 1
        for i in range(1, len(A)):  # B[i] 先逐项乘以左边的A[0],A[1],...,A[i-1]
            temp *= A[i - 1]
            B[i] = temp
        temp = 1
        for i in range(len(A) - 2, -1, -1):  # B[i] 再逐项乘以右边的A[i+1],A[i+2],...,A[n-1]
            temp *= A[i + 1]
            B[i] *= temp
        return B
