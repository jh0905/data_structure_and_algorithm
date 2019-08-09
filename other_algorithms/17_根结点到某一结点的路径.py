# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 10:37
 @desc: DFS + 回溯法
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def find_path(self, root, target, path):
        """
        查找根结点到目标结点的路径，路径用节点的值表示，直接对path进行修改
        :param root: 根结点
        :param target: 目标结点
        :param path: 输入为空列表
        :return: bool
        """
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
    res = []
    sol.find_path(node1, node7, res)
    print(res)
