# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/16 17:18
 @desc: 第83题
"""

"""
 解题思路：
    删除重复节点，但是会保留前面出现的节点，所以头节点必不会被删除，不需要创建虚拟头节点。
    枚举每个节点，有两种情况：
        （1）当前节点之后存在重复节点，删除后面的重复节点
        （2）当前节点不存在重复节点，后移一位
    所以最终p到达None的位置
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head
        p = head
        while p:  # 结束时p为最后一个节点的next节点
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head
