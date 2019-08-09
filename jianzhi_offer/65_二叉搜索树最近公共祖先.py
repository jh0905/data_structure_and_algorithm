# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 20:28
 @desc:
"""


class Solution:

    # 很简单的思路就是看两个值在root的哪边：
    #
    # 两个值都在左边，则LCA在左边
    # 两个值都在右边，则LCA在右边
    # 一个在左一个在右，则说明LCA就是当前的root节点。
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.dfs(root, p, q)

    def dfs(self, root, p, q):
        if not root:
            return root
        if p.val > q.val:  # 保证我们进行搜索时，p的值小于q,简单的交换位置即可
            return self.dfs(root, q, p)
        if p.val <= root.val <= q.val:  # 两个结点在根结点的两边
            return root
        if p.val > root.val:  # 两个结点都在根结点的右侧
            return self.dfs(root.right, p, q)
        if q.val < root.val:  # 两个结点都在根结点的左侧
            return self.dfs(root.left, p, q)
