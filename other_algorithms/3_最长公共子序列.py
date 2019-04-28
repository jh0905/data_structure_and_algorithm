# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/25/19 8:34 AM
 @desc: 最长公共子串（Longest Common Substring）与最长公共子序列（Longest Common Subsequence）的区别：
        子串要求在原字符串中是连续的，而子序列则只需保持相对顺序一致，并不要求连续。
        例如X = 'aQ11' ， Y = 'a11df' ，那么，'a11'是X和Y的最长公共子序列，而'11'是它们的最长公共子串。
"""

"""
 延伸：
    
    最少删除多少个字符使原字符串等成为回文串 等价于 字符串A 与 字符串A的逆序 的最长公共序列为什么?  
  
    如，求alibaba字符串的最长的回文串，等价于 alibaba 和 ababila 的最大公共序列 ababa
 
"""

"""
 最长公共子序列的动态规划状态转移方程：
                        0                       i = 0 or j = 0
                
    LCS(i,j) =  LCS(i-1,j-1) + 1                a[i] == b[j] 且 i,j > 0
     
                max(LCS(i,j-1),LCS(i-1,j))      a[i] != b[j] 且 i,j > 0
"""


# 配合博客：https://blog.csdn.net/yebanxin/article/details/52186706
#         https://blog.csdn.net/littlethunder/article/details/25637173进行阅读
# 最终生成两个二维矩阵
def lcs(str_1, str_2):
    if str_1 == '' or str_2 == '':
        return -1
    m = len(str_1)
    n = len(str_2)
    # 初始化一个行数为(m+1)，列数为(n+1)的零矩阵，记得要用下面方式创建，[[0] * n]*m得到的矩阵有问题，每次赋值是对整列元素赋值
    # 我们增加了最上面添加了一行。最左边添加了一列的目的是因为我们代码运行时，matrix[i+1][j+1]与matrix[i+1][j]或matrix[i][j+1]有关，
    # 如果直接m行n列，那么第0行的元素或者第0列的元素，都没办法计算
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    flag = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # flag矩阵用来标记当前元素是否属于最大公共序列
    for i in range(m):
        for j in range(n):
            if str_1[i] == str_2[j]:
                matrix[i + 1][j + 1] = matrix[i][j] + 1
                flag[i + 1][j + 1] = 'ok'
            elif matrix[i + 1][j] > matrix[i][j + 1]:
                matrix[i + 1][j + 1] = matrix[i + 1][j]
                flag[i + 1][j + 1] = 'left'
            else:
                matrix[i + 1][j + 1] = matrix[i][j + 1]
                flag[i + 1][j + 1] = 'up'
    return matrix, flag


# 得到上述的矩阵之后，我们来思考如何找到对应的最长公共序列
def get_series(string, flag):
    m = len(flag)
    n = len(flag[0])
    i = m - 1
    j = n - 1
    series = []
    while i > 0 and j > 0:
        if flag[i][j] == 'ok':
            series.append(string[i - 1])
            i -= 1
            j -= 1
        elif flag[i][j] == 'left':
            j -= 1
        else:
            i -= 1
    return series


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    mat, flags = lcs(s1, s2)
    print(mat[-1][-1])
    print("".join(get_series(s1, flags)[::-1]))
