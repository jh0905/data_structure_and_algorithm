# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 10:45
 @desc: 第74题
"""


class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        rows = len(matrix)
        cols = len(matrix[0])
        l = 0
        r = rows * cols - 1
        while l < r:
            mid = l + r >> 1
            i = mid // cols
            j = mid % cols
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid
        if matrix[l // cols][l % cols] == target:
            return True
        return False
