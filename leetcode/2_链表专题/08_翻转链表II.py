# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 10:24
 @desc: 第92题
        反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
"""

"""
 解题思路：
     
     对于链表： a -> ... -> p > m -> ... -> n -> q -> ... -> None
    
     第一步：m 到 n 到区间的链表进行翻转，分成了三段
     
     a -> ... -> p   None <- m <- ... <- n    q -> ... -> None
     
     第二步：第m-1个节点的next指针，指向第n个节点，第m个节点的next指针，指向第n+1个节点 
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:

        if not head:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        c = m - 1
        while c:  # p是第m-1个节点，a是第m个节点
            p = p.next
            c -= 1
        cur = p.next
        c = n - m
        while c:
            cur = cur.next
            c -= 1
        q = cur.next  # q是第n+1个节点，
        # 第一步，翻转[m,n]区间的所有节点
        cur.next = None  # 设置循环终止条件
        cur = p.next  # 把cur设为第m个节点，开始进行翻转
        pre = None
        while cur:  # 循环结束后，pre为翻转完的第n个节点
            post = cur.next
            cur.next = pre
            pre = cur
            cur = post
        # 第二步，p指向第n个节点，p.next指向第n+1个节点
        p.next.next = q
        p.next = pre
        return dummy.next
