# Definition for singly-linked list with a random pointer.
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
            p.next = p.next.next
            p = p.next
        return dummy.next
