# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/2/19 7:48 PM
 @desc: 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
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
        return self.dfs(0, len(self.preorder) - 1, 0, len(self.inorder) - 1)

    def dfs(self, pl, pr, il, ir):
        """
        数组范围是闭区间
        pl:前序遍历左边界
        pr:前序遍历右边界
        il:中序遍历左边界
        ir:中序遍历右边界
        """
        if pl > pr:
            return
        root = TreeNode(self.preorder[pl])
        idx = self.inorder.index(self.preorder[pl])
        left = self.dfs(pl + 1, pl + idx - il, il, idx - 1)
        right = self.dfs(pl + idx - il + 1, pr, idx + 1, ir)
        root.left = left
        root.right = right
        return root


if __name__ == '__main__':
    sol = Solution()
    pre_list = [1, 2, 4, 7, 3, 5, 6, 8]
    tin_list = [4, 7, 2, 1, 5, 3, 8, 6]
    print(sol.buildTree(pre_list, tin_list))
