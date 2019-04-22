# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/8/19 2:32 PM
 @desc: 地上有一个m行和n列的方格。一个机器人从坐标0,0的格子开始移动，每一次只能向左，右，上，下四个方向移动一格，
        但是不能进入行坐标和列坐标的数位之和大于k的格子。 例如，当k为18时，机器人能够进入方格（35,37），因为3+5+3+7 = 18。
        但是，它不能进入方格（35,38），因为3+5+3+8 = 19。请问该机器人能够达到多少个格子?
"""


class Solution:
    # 机器人每次能够只能往四个方向进行移动，一开始脑子抽了，直接用遍历来做

    # 算法思路：
    #   首先需要思考我们要定义的几个函数
    #       1.get_num_sum(num)函数，返回某个数的各位元素相加之和
    #       2.check(rows,cols,row,col,threshold,mark_matrix)函数，检查指定的(row,col)元素是否越界，是否小于阈值，是否未被访问过
    #       3.movingCountCore(rows,cols,row,col,threshold,mark_matrix)函数，初始化当前count为0，如果check成功，向四个方向移动
    #           这里用到了一个递归的思想.
    def movingCount(self, threshold, rows, cols):
        if threshold < 0 or rows < 0 or cols < 0:
            return 0
        mark_matrix = [0] * rows * cols
        count = self.movingCountCore(threshold, rows, cols, 0, 0, mark_matrix)
        return count

    def movingCountCore(self, threshold, rows, cols, row, col, mark_matrix):
        count = 0
        if self.check(threshold, rows, cols, row, col, mark_matrix):
            mark_matrix[row * cols + col] = 1
            count = 1 + self.movingCountCore(threshold, rows, cols, row + 1, col, mark_matrix) + \
                    self.movingCountCore(threshold, rows, cols, row - 1, col, mark_matrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col + 1, mark_matrix) + \
                    self.movingCountCore(threshold, rows, cols, row, col - 1, mark_matrix)
        return count

    def check(self, threshold, rows, cols, row, col, mark_matrix):
        if 0 <= row < rows and 0 <= col < cols and self.get_num_sum(
                row) + self.get_num_sum(col) <= threshold and not mark_matrix[row * cols + col]:
            return True
        else:
            return False

    def get_num_sum(self, num):
        result = 0
        while num:
            result += num % 10
            num = num // 10
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.movingCount(10, 1, 100))
