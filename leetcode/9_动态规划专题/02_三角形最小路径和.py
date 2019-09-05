# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/9/4 10:21
 @desc: 第120题
"""

"""
    解题思路：
                     [2]
                    [3,4]
                   [6,5,7]
                  [4,1,8,3]
    根据题意，每一步只能移动到下一行中相邻的结点上，我们用动态规划来做：
    
    - 状态表示：dp[i][j]从起点到第i行第j列个元素的最短路径
    - 状态转移：dp[i][j] = dp[i-1][j-1] + nums[i][j] 从左上角转移过来，要求j>0
              dp[i][j] = dp[i-1][j]，从右上角转移过来，要求j<i
              
    最终遍历最后一层的所有状态，取最小值返回
"""


class Solution:
    def minimumTotal(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        dp[0][0] = nums[0][0]
        for i in range(1, n):
            for j in range(len(nums[i])):
                dp[i][j] = float('inf')
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + nums[i][j])
                if j < i:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j] + nums[i][j])
        ans = float('inf')
        for i in range(n):
            ans = min(dp[-1][i], ans)
        return ans


"""
    可以看到，二维dp数组，每次只涉及到相邻两层的状态，所以我们可以滚动数组，对空间复杂度进行优化，只需要在原来的dp数组
    的基础上，每轮对i&1即可
"""


class Solution:
    def minimumTotal(self, nums):
        n = len(nums)
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = nums[0][0]
        for i in range(1, n):
            for j in range(len(nums[i])):
                dp[i & 1][j] = float('inf')
                if j > 0:
                    dp[i & 1][j] = min(dp[i & 1][j], dp[i - 1 & 1][j - 1] + nums[i][j])
                if j < i:
                    dp[i & 1][j] = min(dp[i & 1][j], dp[i - 1 & 1][j] + nums[i][j])
        ans = float('inf')
        for i in range(n):
            ans = min(dp[n - 1 & 1][i], ans)  # 这里也要滚动转换
        return ans
