# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 09:19
 @desc: 第61题
        给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
"""

"""
 解题思路：
    注意：k的值可能超过链表长度
    
    第一步，求链表长度n，对k取模，k%=n
    
    第二步，把最后一个节点的位置指向空节点
    
    第三步，把倒数第k+1个节点指向空，把倒数第k个节点设为头节点
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return None
        p = head
        q = head
        n = 1
        while p.next:
            p = p.next
            n += 1
        p.next = head  # 把尾结点的next指针，指向头节点
        k %= n
        count = n - k - 1  # 用来统计剩余需要走的长度
        p = head
        while k:
            p = p.next
            k -= 1
        while count:  # q到达倒数第k+1个节点
            p = p.next
            q = q.next
            count -= 1
        new_head = q.next
        q.next = None
        return new_head
