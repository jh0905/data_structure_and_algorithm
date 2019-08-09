# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 11:33
 @desc:
"""


class Solution(object):
    def convert(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        pair = self.dfs(root)
        return pair[0]

    def dfs(self, node):  # 返回以当前节点为根结点的树中，[最左侧的叶子节点，最右侧的叶子节点]
        if not node.left and not node.right:  # 当前节点为叶子结点
            return [node, node]
        if node.left and node.right:
            l_pair = self.dfs(node.left)
            r_pair = self.dfs(node.right)
            l_pair[1].right = node
            node.left = l_pair[1]
            node.right = r_pair[0]
            r_pair[0].left = node
            return [l_pair[0], r_pair[1]]
        if node.left:
            l_pair = self.dfs(node.left)
            l_pair[1].right = node
            node.left = l_pair[1]
            return [l_pair[0], node]
        if node.right:
            r_pair = self.dfs(node.right)
            node.right = r_pair[0]
            r_pair[0].left = node
            return [node, r_pair[1]]
