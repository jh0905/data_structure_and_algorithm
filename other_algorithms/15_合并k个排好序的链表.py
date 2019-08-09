# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/7/31 21:40
 @desc:
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(None)
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1:
            cur.next = l1
        if l2:
            cur.next = l2
        return dummy.next

    def mergeKLists(self, lists):
        # 把k个链表两两合并，用到了栈的操作
        if len(lists) == 0:
            return None
        while len(lists) > 1:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(self.mergeTwoLists(l1, l2))
        return lists.pop()
