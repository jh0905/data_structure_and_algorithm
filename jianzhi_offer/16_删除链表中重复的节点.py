# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/1 14:24
 @desc: 在一个排序的链表中，存在重复的结点，请删除该链表中重复的结点，重复的结点不保留。
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplication(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 创建一个虚拟头节点，避免真正的头节点被删掉
        dummy = ListNode(-1)
        dummy.next = head
        # python分为可变对象赋值和不可变对象赋值
        # 此处是可变对象赋值，p和dummy指向的同一块内存区域，p发生修改，dummy的内容也会跟着修改
        p = dummy
        while p.next:  # 此处的while判断是一个细节，省去了很多麻烦！！！
            q = p.next
            # 初始时，p.next和q指向同一个节点，所以如果q存在，循环一定会执行一次
            while q and p.next.val == q.val:
                q = q.next
            if p.next.next == q:
                p = p.next
            else:
                p.next = q
        return dummy.next
