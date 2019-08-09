# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/2 12:49
 @desc:
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, p1, p2):
        if not p1 or not p2:  # p1,p2一个为空一个不为空或两个同时为空时成立
            return not p1 and not p2  # 只有一个为空返回False，同为空则返回True
        if p1.val != p2.val:  # 两棵树中，对应位置的节点值不相等，直接返回False
            return False
        return self.dfs(p1.left, p2.right) and self.dfs(p1.right, p2.left)
