# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/4/2 23:40
 @desc: 输入一个链表，输出该链表中倒数第k个结点。

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 算法思路：
    #       异常情况分析：k不能等于0，k不能大于链表的长度，链表不能为空
    #       定义两个指针slow，fast，fast指针先走k步
    #       fast走一步，slow走一步
    #       fast指向到终点后的下一个节点的位置时，此时slow指向节点，就是倒数第k个节点
    def FindKthToTail(self, head, k):
        if k == 0 or head is None:
            return None
        fast = slow = head
        # 初始化fast节点的位置，往前移动k位，当k超过链表长度时，返回None
        while k:
            if fast is None:
                return None
            fast = fast.next
            k -= 1
        # fast抵达终点后的下一位置时，此时slow对应的即为倒数第k个节点
        while fast:
            fast = fast.next
            slow = slow.next
        return slow


if __name__ == '__main__':
    node_1 = ListNode(1)
    node_2 = ListNode(3)
    node_3 = ListNode(5)
    node_4 = ListNode(7)
    node_5 = ListNode(9)
    node_1.next = node_2
    node_2.next = node_3
    node_3.next = node_4
    node_4.next = node_5
    node_5.next = None
    sol = Solution()
    print(sol.FindKthToTail(node_1, 1).val)
