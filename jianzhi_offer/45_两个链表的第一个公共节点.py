# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/7 16:52
 @desc:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def findFirstCommonNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p != q:  # 当 p 和 q 相遇的位置，即为第一个公共节点的位置
            p = p.next
            q = q.next
            if not p and not q:  # 同时走到空节点，说明不存在公共节点
                return None
            if not p:  # 只有p走到空节点，让p再去走链表B
                p = headB
            if not q:  # 只有q走到空节点，让q再去走链表A
                q = headA
        return p
