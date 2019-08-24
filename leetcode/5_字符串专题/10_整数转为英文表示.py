# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 22:03
 @desc: 第273题
"""
"""
 解题思路：
    题目给出输入的范围是：0 ～ 2^31-1，即 0 ～ 2,147,483,647
    
    按照英语读法，最高位是 billion，于是我们不妨将输入的整数分为四段：
    
          1~999 billion,   1~999 million,  1~999 thousand,   1~999
          
    接下来，我们要考虑的是1～999 以内的数字如何用英文表示：
         (1) 大于等于100的部分，那就 num//100  +  hundred
         (2) 20~99的部分， num//10的部分转成twenty,thirty,forty  ，num%10的部分，用 one,two，three等表示...
         (3) 0~19的部分，我们创建一个数组，['','one','two','three',...,'nineteen']
    
    所以我们要创建四个数组：
    0～19：['','one','two','three',...,'nineteen']
    0,10,20,30,...,90 : ['', '', 'twenty','thirty','forty',...,'ninety']
    0，1000，1000000，1000000000： ['','thousand','million','billion']
    
    只有输入为0时，才会有zero，其余位置出现的0用''表示。
"""


class Solution:
    def __init__(self):
        self.big = ['Billion', 'Million', 'Thousand', '']
        self.medium = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.small = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven',
                      'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    def numberToWords(self, num: int) -> str:
        if not num:  # 处理输入为0的情况
            return self.small[0]
        res = ''
        i = 1000000000  # 从十亿开始枚举
        j = 0
        while i:
            if num >= i:
                res += self.get_part(num // i) + self.big[j] + ' '
                num = num % i
            i //= 1000
            j += 1
        return res.rstrip()  # 去掉末尾空格，切好为1000，1000000，1000000000时一个空格，其余两个空格

    def get_part(self, num):  # 转换1～999以内的数字
        res = ''
        if num >= 100:
            res = self.small[num // 100] + ' Hundred '
            num %= 100
        if not num:  # num为0要及时返回，避免产生zero
            return res
        if num >= 20:
            res += self.medium[num // 10] + ' '
            num %= 10
        if not num:  # num为0要及时返回，避免产生zero
            return res
        res += self.small[num] + ' '
        return res


if __name__ == '__main__':
    print(Solution().numberToWords(1000))
