# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/19 14:36
 @desc: 第148题
        在 O(n log n)时间复杂度和 O(log n)空间复杂度下，对链表进行排序。

        本题是链表归并排序的模板代码（每个步骤都不可修改，否则会出错，如死循环等）
"""

"""
 解题思路： 
  1. 首先要将将链表分成两等份，用快慢指针实现，mid = slow.next，以及slow.next = None
  
  2. 递归调用归并排序，返回左、右两部分，left = self.sortList(head), right = self.sortList(mid)
  
  3. left 和 right 为归并后的两段有序链表的头节点
  
  4. 创建虚拟头节点dummy，每次选择较小的节点添加到该新链表中
  
  5. 返回归并后的、有序的的新链表，dummy.next
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        # 二分，必须按照这种模板代码
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        mid, slow.next = slow.next, None  # mid为分割后的右半部分的头节点，slow.next=None是把链表断开
        # 递归
        left, right = self.sortList(head), self.sortList(mid)
        # 接下来归并左、右两部分，并返回归并后的头节点
        dummy = ListNode(None)
        p = dummy
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        p.next = left if left else right
        return dummy.next

# 可以看到，每轮在进行归并的时候，都需要创建一个虚拟的头节点，因此空间复杂度为O(log n)
