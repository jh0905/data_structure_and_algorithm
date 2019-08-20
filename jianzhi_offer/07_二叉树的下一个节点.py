# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/2/19 8:28 PM
 @desc: 给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。
        注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针
"""


class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    ########################## 分情况讨论 #############################
    # 1.当前node存在右子树，那么它的下一个节点即为node->next
    # 2.当前node不存在右子树，继续划分为两种情况：
    #   2.1 当前node为father的左儿子，那么它的下一个节点即为 node->father
    #   2.2 当前node为father的右儿子，那么它的下一个节点向上搜索：
    #       2.2.1 如果node->father节点为左儿子，那么它的下一个节点为node->father->father
    #       2.2.2 如果node->father节点为右儿子，继续向上搜索，停止条件为它为左儿子或者到达root节点
    #################################################################

    def getNext_1(self, pNode):
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next

    # 算法思路：
    #       根据中序遍历的思想： 左节点 ->  根节点 -> 右节点
    #       (1)如果某个节点有右子树，那么它的下一个节点则为右子树中的最左子节点
    #       (2)如果某个节点没有右子树，而且它是父节点的右节点，那么我们就往上遍历，直到找到某个节点，满足该节点是其父节点的左子节点，那么程序
    #           要返回的下一个节点则为该节点的父节点，如果找不到满足条件的节点，返回None
    #       (3)如果某个节点没有右子树，并且它是父节点的左节点，那么它的下一个节点则为父节点
    #       (4)如果某个节点没有右子树，并且它是父节点（没有右孩子节点），那么它的下一个节点为None  *** 这个情况很容易漏，要多注意
    def GetNext_2(self, pNode):
        if not pNode:
            return None
        elif pNode.right:  # 对应情况(1)
            pNode = pNode.right
            while pNode.left:
                pNode = pNode.left
            return pNode
        elif pNode.next and pNode.next.right == pNode:  # 对应情况(2)
            while pNode.next and pNode.next.left != pNode:
                pNode = pNode.next
            return pNode.next
        else:  # 对应情况(3)(4)
            return pNode.next
