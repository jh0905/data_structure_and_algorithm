# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 08:58
 @desc: 核心思路：如果当前节点存在左子树，把其左子树的最右侧的路径插入到当前节点的右子树中
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binary_tree_to_linked_list(self, head):
        now = head
        while now:
            if now.left:  # 如果当前节点存在左子树，把其左子树的最右侧的路径插入到当前节点的右子树中
                p = now.left
                while p.right:
                    p = p.right
                p.right = now.right
                now.right = now.left
                now.left = None
            now = now.right
