# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/30 08:42
 @desc: 第652题
"""

"""
    考察二叉树的序列化，哈希表的使用，为了把时间复杂度降到O(n)，我们需要用到两遍哈希。
"""


class Solution:

    def __init__(self):
        self.hash, self.count = {}, {}  # hash用来把子树映射成某个数字，count用来统计子树的个数
        self.cnt = 1
        self.res = []

    def findDuplicateSubtrees(self, root):
        if not root:
            return root
        self.dfs(root)
        return self.res

    def dfs(self, root):
        """
        :param root: 以root为根结点的子树
        :return: 以root为根结点的子树的字符串表示，用'1'，'2'，'3'，'4'，'5' ... 来表示不同的子树
        """
        if not root:
            return "1"  # 1表示空子树，随后的子树用2，3，4，5，...来表示
        left, right = self.dfs(root.left), self.dfs(root.right)  # left和right都对应着某个数字
        subtree = left + " " + str(root.val) + " " + right  # 这里去除空格，最后一个样例通过不了，不知道为什么
        if subtree not in self.hash:
            self.cnt += 1
            self.hash[subtree] = self.cnt  # 第一轮哈希映射，把树的字符串表示映射成某个数字
        t = self.hash[subtree]
        self.count[t] = self.count.get(t, 0) + 1  # 第二轮哈希映射，统计每棵子树出现的次数
        if self.count[t] == 2:  # 出现次数刚好等于2时，把节点添加到res中，避免重复
            self.res.append(root)
        return str(t)
