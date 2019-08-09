# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/2 16:17
 @desc:
"""


class Solution(object):
    def isPopOrder(self, pushV, popV):
        """
        :type pushV: list[int]
        :type popV: list[int]
        :rtype: bool
        """
        stack = []
        flag = True  # 如果本轮中未发生插入或弹出操作，则停止循环
        while flag:
            if stack and popV and stack[-1] == popV[0]:
                flag = False
                stack.pop()
                popV.pop(0)
            elif pushV:
                stack.append(pushV.pop(0))
                flag = False
            flag = True if not flag else False
        if stack:
            return False
        return True


if __name__ == "__main__":
    push = [1, 2, 3, 4, 5]
    pop = [4, 5, 3, 2, 1]
    print(Solution().isPopOrder(push, pop))
