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
class Solution:
    # 算法思路：
    # 这是一个典型的用回溯法来求解的问题：
    # (1)具体步骤如下：
    #   初始化一个长度为矩阵元素个数的零向量，初始path_index = 0
    #   遍历矩阵中的每一个元素
    #       执行havePathCore()操作
    #       如果找到了一条符合要求的路径，返回True,否则继续矩阵中下一个元素的遍历
    #   如果遍历完所有元素，都没有返回True，那么返回False

    # (2)havePathCore()操作如下：
    #   首先判断path_index是否等于path的长度，是的话，说明已经查找路径完毕，返回True,否的话，继续下去
    #   初始bool变量have_path为False
    #   判断条件是否成立，具体如下：
    #       当前矩阵中的元素，所在的row和col是否没有越界；并且矩阵中的该元素是否对应路径中的元素；并且该元素还没有被访问过
    #   条件成立的话，path_index加一，将当前元素标记为已访问，然后递归的往当前元素的四个方向进行搜索，调用hasPathCore()方法;
    #   如果四个方向最终都返回了False的话，将当前元素标记为未访问，然后继续遍历矩阵中的下一个元素
    def hasPath(self, matrix, rows, cols, path):
        if not matrix or rows < 0 or cols < 0 or path is None:
            return False
        mark_matrix = [0] * cols * rows  # 构建一个零向量，用来标记矩阵中的每一个元素
        path_index = 0  # 从路径中第一个元素开始查找
        for row in range(rows):
            for col in range(cols):
                if self.hasPathCore(matrix, rows, cols, row, col, path, path_index, mark_matrix):
                    return True
        return False

    def hasPathCore(self, matrix, rows, cols, row, col, path, path_index, mark_matrix):
        if path_index == len(path):  # 满足条件，则说明path上所有的元素已经查找完毕了
            return True
        has_path = False
        if 0 <= row < rows and 0 <= col < cols and \
                matrix[row * cols + col] == path[path_index] and not mark_matrix[row * cols + col]:
            path_index += 1
            mark_matrix[row * cols + col] = 1
            # 把是否存在指定的路径，结果保存在has_path变量中
            has_path = self.hasPathCore(matrix, rows, cols, row + 1, col, path, path_index, mark_matrix) \
                       or self.hasPathCore(matrix, rows, cols, row - 1, col, path, path_index, mark_matrix) \
                       or self.hasPathCore(matrix, rows, cols, row, col + 1, path, path_index, mark_matrix) \
                       or self.hasPathCore(matrix, rows, cols, row, col - 1, path, path_index, mark_matrix)
            if not has_path:
                path_index -= 1
                mark_matrix[row * cols + col] = 0
        return has_path


if __name__ == '__main__':
    input_matrix = ['a', 'b', 'c', 'e',
                    's', 'f', 'c', 's',
                    'a', 'd', 'e', 'e']
    input_path = ['b', 'c', 'c', 'e', 'd']
    sol = Solution()
    print(sol.hasPath(input_matrix, 3, 4, input_path))
