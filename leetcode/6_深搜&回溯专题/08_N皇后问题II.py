# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 14:45
 @desc: 第52题
        所有皇后，两两之间，不能在同一行、同一列、同一条正对角线、同一条反对角线上
"""

"""
 解题思路：
                    *   *   *   *
                    *   *   *   *
                    *   *   *   *
                    *   *   *   *
    上图是一个 4x4 的棋盘，我们创建一个布尔数组cols = [False] * 4 表示每一列是否放了皇后，
    创建正对角线数组d = [False] * (2 * 4 -1)，反对角线数组ud = d = [False] * (2 * 4 -1)
    
    因为皇后不能在同一行和同一列，我们进行深搜的时候，只需要枚举行，或者枚举列就行了
    dfs(0)，表示从第0行开始搜索，因为逐行枚举，所以一定能保证每个皇后不在同一行中。
    
    然后遍历第0行的每一列，找到一个可以放置的位置，并把对应的布尔数组，全部置为True,再枚举dfs[0+1]
    
    修改rows和cols的布尔值比较简单，如何把 行为i，列为j所在的正对角线和反对角线的布尔值进行修改呢？
    
    观察规律，正对角线的下标为 i+j，反对角线的下标为 i-j+n
    
    于是我们写出深搜+回溯代码了。
"""


class Solution:
    res = 0
    n = 0
    cols = []
    d = []
    ud = []

    def totalNQueens(self, n: int) -> int:
        if not n:
            return 0
        self.res = 0
        self.n = n
        self.cols = [False] * n
        self.d, self.ud = [False] * 2 * n, [False] * 2 * n  # 正对角线下标区间0～2n-2，反对角线1～2n-1
        self.dfs(0)
        return self.res

    def dfs(self, idx):
        if idx == self.n:
            self.res += 1
            return
        for i in range(self.n):
            if not self.cols[i] and not self.d[idx + i] and not self.ud[idx - i + self.n]:
                self.cols[i] = self.d[idx + i] = self.ud[idx - i + self.n] = True
                self.dfs(idx + 1)
                self.cols[i] = self.d[idx + i] = self.ud[idx - i + self.n] = False  # 回溯过程，置为False


if __name__ == '__main__':
    print(Solution().totalNQueens(4))
