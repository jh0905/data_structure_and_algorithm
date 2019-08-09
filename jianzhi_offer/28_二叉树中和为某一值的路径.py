# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/3 15:27
 @desc:
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    res = []
    path = []

    def findPath(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root or not sum:
            return self.res
        self.dfs(root, sum)
        return self.res

    def dfs(self, root, sum):
        if not root:
            return
        self.path.append(root.val)
        sum -= root.val
        if not root.left and not root.right and sum == 0:
            self.res.append(self.path.copy())
        self.dfs(root.left, sum)
        self.dfs(root.right, sum)
        self.path.pop()


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(10)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(12)
    node11 = TreeNode(11)

    node1.left = node2
    node1.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node4.left = node7
    node4.right = node8
    node5.right = node9
    node9.left = node10
    node9.right = node11
    sol = Solution()
    print(sol.findPath(node1, 14))
