# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 20:14
 @desc:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def treeDepth(self, node):
        if not node:
            return 0
        return max(self.treeDepth(node.left), self.treeDepth(node.right)) + 1

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        queue = [root]
        while queue:
            node = queue.pop(0)
            if abs(self.treeDepth(node.left) - self.treeDepth(node.right)) > 1:
                return False
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return True


