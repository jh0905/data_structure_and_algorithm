# encoding: utf-8
"""
 @project:剑指offer_by_Python
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/1/19 8:53 PM
 @desc: 在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，
        输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
"""


class Solution:
    def Find(self, target, array):
        n_rows = len(array)
        n_columns = len(array[0])
        i = n_rows - 1
        j = 0
        while i >= 0 and j < n_columns:
            if array[i][j] == target:
                return True
            elif array[i][j] < target:
                j += 1
            else:
                i -= 1
        return False


if __name__ == '__main__':
    sol = Solution()
    array = [[1, 2, 8, 9],
             [2, 4, 9, 12],
             [4, 7, 10, 13],
             [6, 8, 11, 15]]
    target = 7
    print(sol.Find(target, array))
