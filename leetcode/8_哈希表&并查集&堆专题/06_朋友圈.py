# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 14:54
 @desc: 第547题
"""

"""
    并查集(Union/Find)原理：
    
    从名字可以看出，主要涉及两种基本操作:合并和查找。
    
    初始时，并查集中的元素是不相交的，经过一系列的基本操作(Union)，最终合并成一个大的集合。

    在某次合并之后，有一种合理的需求：某两个元素是否已经处在同一个集合中了？因此就需要Find操作。

    并查集是一种 不相交集合 的数据结构，并查集S由若干子集合si构成，并查集的逻辑结构就是一个森林。
    设有一个动态集合S={s1，s2，s3，.....sn}，si表示森林中的一棵子树,一般以子树的根作为该子树的代表。
    
    比如，若某个元素 x 在集合 s1 中(Find操作)，只需要返回集合 s1 的代表元素即可。这样，判断两个元素是否在同一个集合
    中也是很方便的，只要看find(x) 和 find(y) 是否返回同一个代表即可。

    为什么是动态集合S呢？因为随着Union操作，动态集合S中的子集合个数越来越少。数据结构的基本操作决定了它的应用范围，对
    并查集而言，一个简单的应用就是判断无向图的连通分量个数，或者判断无向图中任何两个顶点是否连通。
    
    由于Find操作需要找到该子集合的代表元素，而代表元素是树根，因此需要保存树中结点的父亲，对于每一个结点，如果知道了父亲，
    沿着父结点链就可以最终找到树根。

    为了简单起见，假设一维数组s中的每个元素 s[i] 表示该元素 i 的父亲。这里有两个需要注意的地方：
        ①我们用一维数组来存储并查集，数组的元素s[i]表示的是结点的父亲的位置。
        ②数组元素的下标 i 则是结点的标识。如：s[5]=4，表示：结点5 的父亲 是结点4。
        
    基本操作实现：
    Union操作就是将两个不相交的子集合合并成一个大集合。
    简单的Union操作是非常容易实现的，只需要把一棵子树的根结点指向另一棵子树即可完成合并，当然，如果选择谁向谁合并，是一个
    可以优化的技术点。    
"""


class Solution:
    p = []  # 一维数组来存储并查集

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def findCircleNum(self, M):
        n = len(M)
        self.p = [-1] * n
        for i in range(n):  # 初始化，每个元素自成一派，属于一个单独的小集合
            self.p[i] = i
        res = n  # 初始时并查集元素个数为n，每合并一次，个数减1
        for i in range(n):
            for j in range(i + 1, n):
                if not M[i][j]:  # i, j不存在边时，跳过。如 i和k相连，j和k相连，此时i和j相连，只需计算相连的边。
                    continue
                if self.find(i) != self.find(j):
                    self.p[self.find(i)] = self.find(j)
                    res -= 1
        return res
