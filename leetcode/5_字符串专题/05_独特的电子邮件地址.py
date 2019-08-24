# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/22 11:15
 @desc: 第929题
"""
"""
 解题思路：
    题目要求返回独一无二的电子邮件个数，我们考虑用set()数据结构，将处理完的电子邮件地址存到集合中。
    
    分两步完成：
        第一：根据'@'符合，将邮件分成左右两部分
        
        第二：对左边部分进行处理，不建议在原字符串上进行修改，因为删除字符串的元素，会导致字符串的长度发生变化，不便枚举
             所以我们创建一个空字符串，遇到不为'.'的字符就加入到新串中，遇到'+'，停止迭代。
    
    然后把新的用户名和邮箱后缀拼接在一起，存到集合中，最后输出集合的元素个数。
"""


class Solution:
    def numUniqueEmails(self, emails):
        s = set()
        for email in emails:
            i = 0
            idx = email.find('@')  # 找到@的索引
            name = ''
            while i < idx:
                if email[i] == '.':
                    i += 1  # 后移一位
                    continue
                if email[i] == '+':
                    break
                name += email[i]
                i += 1
            s.add(name + email[idx:])  # 拼成完整邮件地址，存到集合中，用到add方法
        return len(s)  # 集合有去重的功能


if __name__ == '__main__':
    s = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(s))
