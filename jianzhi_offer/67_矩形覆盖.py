# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/12 10:30
 @desc: 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
"""


# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # 分析
        # 动态规划
        # 状态表示：dp[i]表示n=i时有多少种覆盖方法
        # 状态转移：如果第i-1个小矩形横着放，那么第i个小矩形只能横着放，此时dp[i] += dp[i-2]
        #         如果第i-1个小矩形竖着放，那么第i个小矩形只能横着放，此时dp[i] += dp[i-1]
        # 边界条件：dp[0]=0,dp[1]=1,dp[2]=2,dp[3]=3
        dp = [0, 1, 2] + [0] * (number - 2)
        for i in range(3, number + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[number]
