# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/8/19 9:43 AM
 @desc: 请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
        每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则之后不能再次进入这个格子。
        例如 a b c e
            s f c s
            a d e e
        这样的3 X 4 矩阵中包含一条字符串"bcced"的路径，但是矩阵中不包含"abcb"路径，因为字符串的第一个字符b占据了矩阵中的第一行
        第二个格子之后，路径不能再次进入该格子。
"""


# -*- coding:utf-8 -*-
class Solution(object):
    def hasPath(self, matrix, string):
        """
        :type matrix: List[List[str]]
        :type string: str
        :rtype: bool
        """
        if len(matrix) == 0 or len(matrix[0]) == 0 or len(string) == 0:
            return False
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if self.dfs(matrix, string, 0, row, col):
                    return True
        return False

    def dfs(self, matrix, path, path_idx, x, y):
        """
        :param matrix: 输入矩阵
        :param path: 输入路径
        :param path_idx: 待查找路径中的元素下标
        :param x: 暴搜法的矩阵元素横坐标
        :param y: 暴搜法的矩阵元素纵坐标
        :return:
        """
        if matrix[x][y] != path[path_idx]:
            return False
        if path_idx == len(path) - 1:
            return True
        temp = matrix[x][y]
        matrix[x][y] = "*"  # 把矩阵中的元素设为不存在的元素，避免它被重复使用
        dx = [-1, 1, 0, 0]
        dy = [0, 0, 1, -1]
        # 寻找上下左右四个方向，是否存在一个点为路径中的下一个元素
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < len(matrix) and 0 <= b < len(matrix[0]):
                if self.dfs(matrix, path, path_idx + 1, a, b):
                    return True
        matrix[x][y] = temp  # 还原矩阵原始值
        return False


if __name__ == '__main__':
    input_matrix = [['b', 'b', 'c', 'e'],
                    ['s', 'f', 'c', 's'],
                    ['a', 'd', 'e', 'e']]
    input_path = ['b', 'c', 'c', 'e', 'd']
    sol = Solution()
    print(sol.hasPath(input_matrix, input_path))
