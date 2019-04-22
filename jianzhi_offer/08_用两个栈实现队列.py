# encoding: utf-8
"""
 @project:Data_Structure&&Algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/2/19 9:18 PM
 @desc: 用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型
"""


class Solution:
    # 算法思路：
    #       队列的特性：first in first out ， 栈的特性：last in first out
    #       有两个栈stackA,stackB，A为入栈，B为出栈的；
    #       入栈时，直接进入A即可；
    #       出栈时，先判断B中是否有元素，如果没有则不能pop()，应将A中所有元素倒压在B里面，再pop()最上面（后面）的元素
    #                               如果有，直接pop()就可以了
    def __init__(self):
        self.stackA = []
        self.stackB = []

    def push(self, node):
        self.stackA.append(node)

    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()


if __name__ == '__main__':
    sol = Solution()
    sol.push(1)
    sol.push(2)
    sol.push(3)
    print(sol.pop())
    print(sol.pop())
    sol.push(4)
    sol.push(5)
    print(sol.pop())
    print(sol.pop())
    print(sol.pop())
