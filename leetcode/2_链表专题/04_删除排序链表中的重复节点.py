# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 17:35
 @desc: 第82题
"""

"""
 解题思路：
    本题和上一题的区别在于，如果存在重复节点，那么把重复节点全部删除。
    所以存在头节点会被删除的情况，我们需要创建虚拟头节点。
    
    定义一个指针p指向虚拟头节点，p指针始终指向链表中，从前往后，不含重复节点的某个节点
    
    枚举节点p，用q指向p的下一个节点，当q存在且q的值等于p的下一个节点
    
    分情况讨论：
        p,q节点间距为2，说明p的下一个节点一定不是重复节点，将指针p指向它的下一个节点
        p,q节点间距大于2，将p的next指针指向q
        
    所以最终p到达最后一个不为重复节点的位置
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head
        p = dummy
        while p.next:
            q = p.next
            while q and p.next.val == q.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return dummy.next
