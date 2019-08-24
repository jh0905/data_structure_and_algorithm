# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 17:17
 @desc: 第6题
"""

"""
 解题思路：找规律
    我们输入字符串为helloworld，行数为4
                       
                        h    o
                        e  w r 
                        l o  l
                        l    d
    
    初始时，res = ['', '', '', ''] ,idx = 0
    
    字符： h  e  l  l  o  w  o  r   l   d
    索引： 0  1  2  3  2  1  0  1   2   3 
    
    最终， res = ['ho', 'ewr', 'lol', 'ld']，拼接起来，即为我们的返回结果。
    
    那我们的目标，就是要找到idx值的变换规律。
    当 idx = 0时，我们后面自增1
    当 idx = numRows-1时，我们后面自减1
    
    然后就可以完成代码了。    
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 3 or numRows == 1:
            return s
        res = [''] * numRows
        idx, step = 0, 1
        for ch in s:
            if idx == 0:
                step = 1
            elif idx == numRows - 1:
                step = -1
            res[idx] += ch
            idx += step
        return ''.join(res)
