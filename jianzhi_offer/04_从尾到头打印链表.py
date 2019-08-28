# encoding: utf-8
"""
 @project:剑指offer_by_Python
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/1/19 9:45 PM
 @desc: 输入一个链表，按链表值从尾到头的顺序返回一个ArrayList。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    res = []

    # 递归的思想
    def printListFromTailToHead(self, listNode):
        self.res = []
        if not listNode:
            return
        else:
            self.printListFromTailToHead(listNode.next)
            self.res.append(listNode.val)
        return self.res


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(2)
    node_3 = ListNode(3)
    node_4 = ListNode(4)
    node_5 = ListNode(5)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = None
    sol = Solution()
    print(sol.printListFromTailToHead(node_1))
