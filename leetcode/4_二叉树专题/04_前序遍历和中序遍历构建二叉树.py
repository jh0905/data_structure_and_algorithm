# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 14:38
 @desc:
"""
"""
 解题思路就不用多说了，主要是用到了递归的思想，把区间按照左右子树进行划分，然后递归地构建左右子树，最终返回头节点。
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    preorder = []
    inorder = []

    def buildTree(self, _preorder, _inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.preorder = _preorder
        self.inorder = _inorder
        if not self.preorder:
            return None
        return self.dfs(0, len(self.preorder) - 1, 0, len(self.inorder) - 1)

    def dfs(self, pl, pr, il, ir):
        if pl > pr:
            return
        root = TreeNode(self.preorder[pl])
        idx = self.inorder.index(self.preorder[pl])
        root.left = self.dfs(pl + 1, pl + idx - il, il, idx - 1)
        root.right = self.dfs(pl + idx - il + 1, pr, idx + 1, ir)
        return root
