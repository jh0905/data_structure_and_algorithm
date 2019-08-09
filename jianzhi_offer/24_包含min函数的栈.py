# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/2 15:10
 @desc:
"""


class MinStack(object):

    def __init__(self):
        self.stack = []  # 普通栈
        self.min_stack = []  # 辅助栈，单调递减栈

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)  # 普通栈，直接将元素入栈
        # 如果辅助栈为空或者它的栈顶元素不小于当前元素，则将元素入栈
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
