# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 20:15
 @desc:
"""


class Solution(object):
    ans = True

    def treeDepth(self, node):
        if not node:
            return 0
        left = self.treeDepth(node.left)
        right = self.treeDepth(node.right)
        if abs(left - right) > 1:
            self.ans = False
            return
        return max(left, right) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        self.treeDepth(root)
        return self.ans
