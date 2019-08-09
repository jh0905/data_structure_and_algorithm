# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/9 20:31
 @desc:
"""


class Solution(object):
    def strToInt(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0
        k = 0
        while str[k] == ' ':  # 1.去开头空格
            k += 1
        str = str[k:]
        is_positive = True
        if str[0] == '-':  # 2. 如果存在正负号，记录下来，并去掉
            is_positive = False
            str = str[1:]
        elif str[0] == '+':
            str = str[1:]
        number = 0
        for i in range(len(str)):  # 将数值部分的字符串转成int存储
            if '0' <= str[i] <= '9':  # 判断字符是否为数值
                number = number * 10 + ord(str[i]) - ord('0')
            else:
                break
        if number <= 2 ** 31 - 1:
            return number if is_positive else -number
        else:
            return 2 ** 31 - 1 if is_positive else -2 ** 31


if __name__ == '__main__':
    print(Solution().strToInt('         -1272178asbxjabscua'))
