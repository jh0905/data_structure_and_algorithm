# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 17:25
 @desc: 第155题
"""

"""
    本题考察单调递减栈的使用
"""


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []  # 单调递减栈，栈顶元素是栈的最小元素

    def push(self, x: int) -> None:
        if not self.min_stack or self.min_stack[-1] >= x:
            self.min_stack.append(x)
        self.stack.append(x)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
