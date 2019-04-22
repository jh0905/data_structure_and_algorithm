# encoding: utf-8
"""
 @project:剑指offer_by_Python
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/1/19 9:05 PM
 @desc: 请实现一个函数，将一个字符串中的每个空格替换成“%20”。例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy
"""


class Solution:
    # s 源字符串

    # 算法思路：
    #   空格占一个字符，替换的"%20"占三个字符，就是说最终字符串的长度新增加了2*空格数
    #   创建新的字符串列表，一个指针p_1指向原数组的末尾，一个指针p_2指向新数组的末尾
    #   当p_1>=0时：
    #       如果p_1指向的元素不是空格，那么s[p_2]=s[p_1]，并把p_2前移一位
    #       否则：
    #           把s[p_2]的元素值依次赋值为'0','2','%'，p_2前移三位
    #       p_1指向的元素前移一位

    def replaceSpace(self, s):
        s = list(s)  # python中原字符串是一个常量，无法修改，所以只能转成list形式,最后返回时用''.join(s)还原成字符串
        # 计算空格数量
        count = 0
        for c in s:
            if c == ' ':
                count += 1
        p_1 = len(s) - 1
        s += [None] * 2 * count
        p_2 = len(s) - 1
        while p_1 >= 0:
            if s[p_1] != ' ':
                s[p_2] = s[p_1]
                p_2 -= 1
            else:
                for i in ['0', '2', '%']:
                    s[p_2] = i
                    p_2 -= 1
            p_1 -= 1
        return ''.join(s)


if __name__ == '__main__':
    sol = Solution()
    s = 'we are happy'
    print(sol.replaceSpace(s))
