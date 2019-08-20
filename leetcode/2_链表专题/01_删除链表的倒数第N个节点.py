# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 16:35
 @desc:
"""

"""
 单链表删除：
    待删节点的前驱节点的next指针，指向待删节点的后继节点
    
 解法流程：
    凡是有可能删除头节点的情况
  1. 建立虚拟头节点，指向真正的头节点
  2. 设置双指针都指向虚拟头节点
  3. first指针先走n步
  4. second指针也开始走，两个指针同时一次移动一步
  5. first到达最后一个节点时，second刚好到达倒数第(n+1)个节点的位置
  6. 删除倒数第n个节点
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)  # step1
        dummy.next = head
        p = dummy  # step2
        q = dummy
        while n:  # step 3
            p = p.next
            n -= 1
        while p.next:  # step 4,5
            p = p.next
            q = q.next
        q.next = q.next.next  # step 6 删除倒数第n个节点
        return dummy.next
