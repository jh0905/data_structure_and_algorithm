# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/3 18:29
 @desc:
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    res = []
    path = []

    def find_path(self, root, target):
        self.res = []
        if not root or not target:
            return self.res
        self.dfs(root, target)

    def dfs(self, root, target):
        if not root:
            return
        self.path.append(root.val)
        if root.val == target.val:
            self.res = self.path.copy()
            return
        self.dfs(root.left, target)
        self.dfs(root.right, target)
        self.path.pop()


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
    sol.find_path(node1, node7)
    print(sol.res)
