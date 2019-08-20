# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 10:14
 @desc: 第206题
        翻转一个单链表，简单题
"""

"""
 解题思路：
  如 链表： a -> b -> c  -> d -> None
    cur 指向 a
    post = cur.next 存储当前节点的下一个节点b
    a.next = pre (初始pre为None)
    pre = a
    cur = post
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        #
        if not head:
            return head
        pre = None
        cur = head
        while cur:
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        return pre
