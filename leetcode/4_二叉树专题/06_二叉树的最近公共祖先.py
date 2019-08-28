# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 15:02
 @desc: 第236题
"""

"""
 解题思路：
    在大体上，p,q,root的情况有三种情况，p,q在root的两侧，p,q同在root的左侧，p,q同在root的右侧。
        
    最近公共节点的分布有两种情况：
        (1)p和q分布在根结点的两侧，那么最近公共节点为该根结点
        (2)p是q的祖先或者q是p的祖先，那么最近公共节点为p或q
    
    于是我们递归左右子树，如果为空，或者找到某个节点为p或者q时则返回
    
    如果返回的left和right都不为空，说明p,q在根结点两侧
    
    如果一方为空，说明某个节点是另一个节点的祖先。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        # 题目给出p,q一定是树中的节点，所以我们直接用root==p判断是否相等，而不是用root.val == p.val，因为可能存在重复元素
        if not root or root == p or root == q:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if left and right:
            return root
        return left if left else right
