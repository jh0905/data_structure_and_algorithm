# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 11:02
 @desc: 第165题
"""

"""
 解题思路：
    一个简单的思路是，调用split(".")函数，把字符串按照'.'进行切割，然后把切割完的list中每个元素转成int,并补在末尾补0
    使得两个list长度相等。
    
    但是本专题是字符串处理，调用split()难免有些偷懒的嫌疑，于是我们跟前面一样，使用分段模板代码，将字符串进行划分。
    
    第一个注意点，大循环是 i < len(s1) or j < len(s2) 只有有字符串未切割完，则继续切割
    
    第二个注意点，可能存在一个切割完，得到空串""，我们进行判断，将空串转为0
    
    第三个注意点，最终 i，j 赋值时，要跳过'.'号，所以 i, j = x + 1, y + 1
"""


class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        i, j = 0, 0
        while i < len(s1) or j < len(s2):
            x, y = i, j
            while x < len(s1) and s1[x] != '.':  # 分段模板代码
                x += 1
            while y < len(s2) and s2[y] != '.':
                y += 1
            a = int(s1[i:x]) if x > i else 0  # 存在为空的情况，转换成0
            b = int(s2[j:y]) if y > j else 0
            if a < b:
                return -1
            if a > b:
                return 1
            i, j = x + 1, y + 1
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion('1.0', '1.1'))
