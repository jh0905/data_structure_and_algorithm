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
    def get_num(self, x):
        num = 0
        while x:
            num += x % 10
            x = x // 10
        return num

    def check(self, threshold, x, y):
        """
        判断当前格子下标的数值和是否大于阈值
        :param threshold:
        :param x:
        :param y:
        :return: bool
        """
        if self.get_num(x) + self.get_num(y) > threshold:
            return True
        return False

    def movingCount(self, threshold, rows, cols):
        res = 0
        if threshold < 0 or rows <= 0 or cols <= 0:
            return res
        label_mat = [[0] * cols for _ in range(rows)]  # 初始化label矩阵，用来标记当前元素是否已访问
        queue = [[0, 0]]  # 初始化BFS搜索队列，首先喂进去矩阵中的第一个元素
        dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
        while queue:
            x, y = queue.pop(0)  # 弹出队列中的队首元素的坐标
            # 检查当前元素是否已访问（因为搜索队列中某个元素可能被重复添加）or 矩阵下标大于阈值，为障碍物，不能移动！
            if label_mat[x][y] == 1 or self.check(threshold, x, y):
                continue
            res += 1
            label_mat[x][y] = 1  # 将矩阵中的当前元素标记为已访问
            for i in range(4):
                a = x + dx[i]
                b = y + dy[i]
                if 0 <= a < rows and 0 <= b < cols and label_mat[a][b] == 0:
                    queue.append([a, b])
        return res


if __name__ == '__main__':
    sol = Solution()
    print(sol.movingCount(3, 13, 14))
