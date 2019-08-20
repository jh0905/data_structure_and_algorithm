# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 09:54
 @desc: 第24题
"""

"""
 解题思路：
    链表类型的题，思路最重要，要先想明白指针的变换顺序
    头节点位置可能会发生变换，所以我们设置一个虚拟头节点指向真正的头节点，用cur指向dummy
    如：dummy -> a -> b -> c -> d -> e -> None
    cur = dummy
    p = a  
    1. cur的next指向b
    2. a的next指向c
    3. b的next指向a
    4. cur = a
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        if not head:
            return head
        cur = dummy
        while cur.next:
            p = cur.next
            if not p.next:  # 如果最后只剩下一个节点，不执行交换过程，退出循环
                break
            cur.next = cur.next.next
            p.next = p.next.next
            cur.next.next = p
            cur = p
        return dummy.next
