# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/5 10:24
 @desc:
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        # 第一步，复制新节点在原节点之后
        cur = head
        while cur:
            p = ListNode(cur.val)
            p.next = cur.next
            cur.next = p
            cur = p.next
        # 第二步，复制新节点的random指针
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next  # cur每次都指向原节点，跨一个节点移动
        # 第三步，分离链表
        dummy = ListNode(None)
        cur = dummy
        p = head
        while p:
            cur.next = p.next
            cur = cur.next
            p = p.next.next  # 跨节点移动
        return dummy.next
