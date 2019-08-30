# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 15:44
 @desc: 第684题
        输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的 树 及 1条附加的边 构成。

        附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。
"""

"""
    解题思路：并查集
    
    每传入一组边，判断两个点是否在同一个集合内，是的话，则直接返回这条边，否则将两个点的集合合并。
"""


class Solution:
    p = []

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def findRedundantConnection(self, edges):
        n = len(edges)  # 输入N条边，则树中有n个节点（题目要求），编号从1开始
        self.p = [-1] * (n + 1)
        for i in range(1, n + 1):
            self.p[i] = i
        for edge in edges:
            if self.find(edge[0]) != self.find(edge[1]):
                self.p[self.find(edge[0])] = self.find(edge[1])
            else:
                return edge
