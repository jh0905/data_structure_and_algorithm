# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 10:32
 @desc: 第17题
"""

"""
 解题思路：
    
    本题我采用的是深搜+回溯的思想进行求解。
    
    输入的是digits，我们要求解的是，所有字母的组合情况。
    
    考虑深搜的话，必须先想清楚dfs停止的条件，像这种题目我们之前做过，可以用index作为判断，每次dfs下一轮时，则把index+1
    
    在每一轮的时候，我们找到本轮待枚举的字符串，用 self.s[int(digits[idx])] 得到，然后枚举每一个字符，枚举完了之后，考虑
    
    回溯过程，这里把上一步添加的字符弹出即可，用self.ans.pop()可以完成
"""


class Solution:

    def __init__(self):
        self.res = []  # 收集每一种可能的组合
        self.ans = []  # 记录单个组合
        self.s = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def letterCombinations(self, digits):
        if not digits:
            return []
        self.dfs(digits, 0)
        return self.res

    def dfs(self, digits, idx):
        if idx == len(digits):
            self.res.append(''.join(self.ans))
            return  # 返回到上一层
        chars = self.s[int(digits[idx])]
        for i in range(len(chars)):
            self.ans.append(chars[i])
            self.dfs(digits, idx + 1)
            self.ans.pop()  # 回溯


if __name__ == '__main__':
    print(Solution().letterCombinations('234'))
