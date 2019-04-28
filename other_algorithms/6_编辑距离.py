# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/26/19 1:57 PM
 @desc: 编辑距离，又称Levenshtein距离，是指两个字串之间，由一个转成另一个所需的最少编辑操作次数，
                                    (1 - 编辑距离/两个字符串长度的最大值) 反映了它们之间的相似性
        一共有三种操作：
            如'abcd' -> 'acd' 只需要进行一次删除操作
              'ac'  -> 'abc' 只需要进行一次插入操作
              'abc' -> 'abd' 只需要进行一次替换操作
"""


# 参考 https://www.dreamxu.com/books/dsa/dp/edit-distance.html
#      https://leetcode-cn.com/problems/edit-distance/comments/64379

# 时间复杂度O(mn)，空间复杂度O(n^2)
def min_distance(string_1, string_2):
    m, n = len(string_1), len(string_2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = 0
    for i in range(1, m + 1):
        dp[i][0] = i
    for j in range(1, n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if string_1[i - 1] == string_2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
    return dp[m][n]


# 时间复杂度O(mn)，空间复杂度O(n)
def min_distance_2(string1, string2):
    m, n = len(string1), len(string2)
    dp1 = [0] * (n + 1)  # 保留两行
    dp2 = [0] * (n + 1)
    dp1[0] = 0
    for j in range(1, n + 1):
        dp1[j] = j
    for i in range(1, m + 1):
        dp2[0] = i
        for j in range(1, n + 1):
            if string1[i - 1] == string2[j - 1]:
                dp2[j] = dp1[j - 1]
            else:
                dp2[j] = min(dp1[j], dp2[j - 1], dp1[j - 1]) + 1
        dp1, dp2 = dp2, dp1
    return dp1[n]


# 时间复杂度O(mn)，空间复杂度O(n)
def min_distance_3(string1, string2):
    m, n = len(string1), len(string2)
    dp = [0] * (n + 1)  # 保留一行
    dp[0] = 0
    for j in range(1, n + 1):
        dp[j] = j
    for i in range(1, m + 1):
        old_dp_j = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            old_dp_j_1, old_dp_j = old_dp_j, dp[j]
            if string1[i - 1] == string2[j - 1]:
                dp[j] = old_dp_j_1
            else:
                dp[j] = min(dp[j], dp[j - 1], old_dp_j_1) + 1
    return dp[n]


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(min_distance(s1, s2))
    print(min_distance_2(s1, s2))
    print(min_distance_3(s1, s2))
