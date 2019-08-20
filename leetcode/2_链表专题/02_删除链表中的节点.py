# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 17:02
 @desc: 第237题
        请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。
"""

"""
 解题思路：
    正常来说，删除链表中的一个节点，要先找到它的前驱节点，前驱节点的next指针指向该节点的下一个节点
    这里没有办法获得前驱节点，那就只能换个思路，把当前节点的值存为它的下一个节点值，再删除它的下一个节点。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        next = node.next
        node.val = next.val
        node.next = next.next
