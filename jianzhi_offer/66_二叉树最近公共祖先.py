# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 20:28
 @desc:
"""


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root or p == root or q == root:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left and right:
            return root
        return left if left else right
