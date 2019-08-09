# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/2 11:14
 @desc: 本题有个特点，就是镜像二叉树是把原来的二叉树的左右节点全部交换
"""


class Solution(object):
    def mirror(self, root):
        """
        :type root: TreeNode
        :rtype: void
        """
        if not root:
            return
        temp = root.left
        root.left = root.right
        root.right = temp
        self.mirror(root.left)
        self.mirror(root.right)
