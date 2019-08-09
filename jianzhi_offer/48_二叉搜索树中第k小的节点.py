# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 19:52
 @desc:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    ans = TreeNode(-1)
    k = 0  # 必须将k存为全局变量，因为每轮递归回退时的k不是同一个k值

    def dfs(self, root):
        if not root:
            return
        self.dfs(root.left)
        self.k -= 1
        if not self.k:
            self.ans = root
            return  # 找到第k小的节点之后，可以提前返回，不需要再往下遍历了
        self.dfs(root.right)

    def kthNode(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: TreeNode
        """
        self.k = k
        self.dfs(root)
        return self.ans
