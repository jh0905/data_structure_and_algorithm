# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/2 14:28
 @desc:
"""


class Solution(object):
    def printMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return matrix
        m = len(matrix)
        n = len(matrix[0])
        label_mat = [[0] * n for _ in range(m)]
        res = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x, y, direction = 0, 0, 0
        for i in range(0, m * n):
            res.append(matrix[x][y])
            label_mat[x][y] = 1
            a = x + dx[direction]
            b = y + dy[direction]
            if a < 0 or a >= m or b < 0 or b >= n or label_mat[a][b]:
                direction = (direction + 1) % 4
                a = x + dx[direction]
                b = y + dy[direction]
            x = a
            y = b
        return res
