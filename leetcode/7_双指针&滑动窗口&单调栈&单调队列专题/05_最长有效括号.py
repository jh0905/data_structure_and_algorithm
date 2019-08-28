# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 16:12
 @desc: 第32题
"""

"""
 解题思路： ***
    
    括号序列类型的题，必须牢记一个重要的性质：
        
    括号序列合法 等价于 我们如果把左括号看成是+1，右括号看成是-1，那么合法的括号序列满足所有前缀和>=0,并且总和等于0。
    
    算法流程：
        定义一个cnt=0 
        定义指针i, 从左到右枚举序列中的每一个元素，如果s[i]=='(',cnt+=1；如果s[i]==')',cnt-=1
        
        如果 cnt < 0: 说明当前序列不合法，我们令 start = i + 1, cnt重置为0
        如果 cnt > 0: 继续往后移动i
        如果 cnt == 0，说明从start到i的这段序列是合法的括号序列，保存下来，记录其长度
        
    注意：存在 cnt 始终大于0的情况，如 (((())，那么我们把原序列翻转一遍，并把左、右括号交换，得到(())))，再计算一遍它的
    最长合法括号序列即可。
"""


class Solution:
    def compute(self, s):
        cnt = 0
        start = 0
        res = 0
        for i in range(len(s)):
            if s[i] == '(':
                cnt += 1
            else:
                cnt -= 1
                if cnt < 0:
                    cnt = 0
                    start = i + 1
                elif cnt > 0:
                    continue
                else:
                    res = max(res, i - start + 1)
        return res

    def longestValidParentheses(self, s: str) -> int:
        res1 = self.compute(s)
        s = list(s)[::-1]
        for i in range(len(s)):
            s[i] = chr(ord(s[i]) ^ 1)  # "("对应的ascii码为40，")"对应的ascii码为41，40^1=41，41^1=40
        return max(res1, self.compute(s))


if __name__ == '__main__':
    print(Solution().longestValidParentheses(')()())'))
