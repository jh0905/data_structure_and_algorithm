# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 12:59
 @desc: 输入的二叉树为普通的二叉树，
        【朴素解法】 找出两个节点的路径，然后找到最近的公共祖先
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def find_path(self, root, target, path):
        if not root or not target:
            return False
        path.append(root.val)
        if root.val == target.val:
            return True
        if root.left:
            if self.find_path(root.left, target, path):
                return True
        if root.right:
            if self.find_path(root.right, target, path):
                return True
        # 回溯，删除不在路径中的节点
        path.pop()
        return False

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path_1 = []
        path_2 = []
        self.find_path(root, p, path_1)
        self.find_path(root, q, path_2)
        print(path_1)
        print(path_2)
        i = 0
        while i < min(len(path_1), len(path_2)):
            if path_1[i] != path_2[i]:
                return path_1[i - 1]
            i += 1
        return path_1[-1] if len(path_1) < len(path_2) else path_2[-1]


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node2.left = node4
    node3.right = node5
    node5.left = node6
    node5.right = node7
    sol = Solution()
    res = sol.lowestCommonAncestor(node1, node3, node7)
    print(res)
