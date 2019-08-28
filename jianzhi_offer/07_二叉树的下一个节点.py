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
    # 1.当前node存在右子树，那么它的下一个节点即为右子树的最左节点，node->next
    # 2.当前node不存在右子树，继续划分为两种情况：
    #   2.1 当前node为father的左儿子，那么它的下一个节点即为 node->father
    #   2.2 当前node为father的右儿子，那么它的下一个节点向上搜索：
    #       2.2.1 如果node->father节点为左儿子，那么它的下一个节点为node->father->father
    #       2.2.2 如果node->father节点为右儿子，继续向上搜索，停止条件为它为左儿子或者到达root节点
    #################################################################

    def getNext(self, pNode):
        if pNode.right:
            p = pNode.right
            while p.left:
                p = p.left
            return p
        while pNode.next and pNode.next.right == pNode:
            pNode = pNode.next
        return pNode.next
