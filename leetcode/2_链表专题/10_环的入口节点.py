# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 11:27
 @desc: 第142题
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        p = head
        q = head
        while q:
            p = p.next
            q = q.next  # 这里是细节，走两步的判断
            if q:
                q = q.next
            else:  # 说明不存在环
                break
            if p == q:  # 相遇说明存在环
                p = head
                while p != q:
                    p = p.next
                    q = q.next
                return p
        return None
