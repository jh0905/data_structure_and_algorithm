# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 11:24
 @desc: 第160题
"""

"""
 解题思路：
     定义两个指针p,q，p指向headA，q指向headB
     两个指针同时走，如果同时走向空，说明不相交，否则走向空的指针，再从另一个链表的头节点开始走
     如果存在交点，那么两个指针必定会在交点相遇
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        p = headA
        q = headB
        while p != q:
            p = p.next
            q = q.next
            if not p and not q:
                return None
            if not p:
                p = headB
            if not q:
                q = headA
        return p
