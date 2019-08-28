# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/21 14:45
 @desc: 第102题

        二叉树的层次遍历模板代码
"""


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root, None]
        res = []
        layer = []
        while queue:
            node = queue.pop(0)  # 层次遍历每次弹出队首元素
            if not node:
                if not layer:  # 此处十分重要，在遍历完最后一层时，layer为空，作为退出循环的条件
                    break
                res.append(layer)  # 如果下面用clear()方法，这里要存layer的备份，可以用layer[::]代替layer.copy()
                layer = []  # 这里要用layer=[]，而不是layer.clear()，二者的意义是有很大差别的。
                queue.append(None)
                continue  # 结束本轮循环
            layer.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return res
