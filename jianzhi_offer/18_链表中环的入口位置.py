# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/1 15:53
 @desc:
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def entryNodeOfLoop(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        q = head
        while p and q:
            p = p.next
            q = q.next
            if q:
                q = q.next
            else:  # 说明不存在环，q抵达尾节点
                return None
            if p == q:  # 说明链表存在环
                p = head
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
