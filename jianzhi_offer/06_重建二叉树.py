# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/2/19 7:48 PM
 @desc: 输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
        例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回构造的TreeNode根节点

    # 算法思路：
    #    前序遍历的第一个元素为根节点的值，中序遍历列表中，根节点的值在中间，左边的为左子树的所有节点，右边为右子树的所有节点
    #    然后用递归的思路，重复上面的过程
    #    如果 pre为空或者tin为空，返回None (排除异常情况)
    #    否则：
    #       root = pre[0]
    #       pos = tin.index(pre[0])   # 根节点在中序列表的position
    #       root.left = 递归调用(pre[1:pos+1],tin[:pos])
    #       root.right = 递归调用(pre[pos+1:],tin[pos+1:])
    #    递归结束，返回root
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre[0])
        pos = tin.index(pre[0])
        root.left = self.reConstructBinaryTree(pre[1:pos + 1], tin[:pos])
        root.right = self.reConstructBinaryTree(pre[pos + 1:], tin[pos + 1:])
        return root


if __name__ == '__main__':
    sol = Solution()
    pre_list = [1, 2, 4, 7, 3, 5, 6, 8]
    tin_list = [4, 7, 2, 1, 5, 3, 8, 6]
    print(sol.reConstructBinaryTree(pre_list, tin_list))
