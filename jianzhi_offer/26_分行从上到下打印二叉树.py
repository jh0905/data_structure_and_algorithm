# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 09:51
 @desc: 是一种经典的BFS算法，它的变种是蛇形遍历！
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def printFromTopToBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:  # 异常情况排除
            return res
        queue = [root, None]
        level = []
        while queue:
            node = queue.pop(0)
            if not node:  # 遇到我们设定的None，说明本层节点遍历完毕
                if not level:
                    break  # 如果level为空，说明队列遍历完毕，结束循环
                res.append(level.copy())
                level.clear()
                queue.append(None)  # 插入到遍历队列中，作为一层结束的标记
                continue  # 结束本轮循环
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res

    def printFromTopToBottom_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:  # 异常情况排除
            return res
        queue = [root, None]
        level = []
        i = 1  # 用来
        while queue:
            node = queue.pop(0)
            if not node:  # 遇到我们设定的None，说明本层节点遍历完毕
                if not level:
                    break  # 如果level为空，说明队列遍历完毕，结束循环
                i += 1
                res.append(level[::pow(-1, i)])
                level = []
                queue.append(None)  # 插入到遍历队列中，作为一层结束的标记
                continue  # 结束本轮循环
            level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res


if __name__ == "__main__":
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node9 = TreeNode(9)
    node10 = TreeNode(10)
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
    print(sol.printFromTopToBottom(node1))
    print(sol.printFromTopToBottom_2(node1))
