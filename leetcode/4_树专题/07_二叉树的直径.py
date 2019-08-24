# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 15:25
 @desc:
"""
"""
    这一题和判断二叉树是否为平衡二叉树的思路近似，都需要用到求解二叉树的深度的模板代码。
    
    在本题中，二叉树的直径即为左右子树深度和最大的值。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.res = 0
        self.dfs(root)
        return self.res

    # 求二叉树的深度,顺便记录左右子树深度和最大的值，即为直径
    def dfs(self, root):
        if not root:
            return 0
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        self.res = max(self.res, left + right)
        return max(left, right) + 1
