# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/23 16:38
 @desc: 第78题 输入的list中，不存在重复元素，输出所有子集的list
"""

"""
 解题思路1：
    我们先考虑用迭代的做法：
    
    给定集合{1, 2, 3}，它的子集有：
            {}
            {1}, {2}, {3}
            {1,2}, {1,3}, {2,3}
            {1,2,3}  
    一共有 2^3 = 8 个子集
    
    在涉及到集合的子集问题时，我们考虑二进制的使用，0 ~ 2^3-1 之间有8个元素，二进制表示为：
            000  -> {}         num >> 0,1,2都没有1
            001  -> {1}        num >> 0 得 1，  {nums[0]}
            010  -> {2}        num >> 1 得 1，  {nums[1]}
            011  -> {1,2}      num >> 0,1得1，  {nums[0],nums[1]}
            100  -> {3}        num >> 2 得1，   {nums[2]}
            101  -> {1,3}      num >> 0,2得1，  {nums[0],nums[2]}
            110  -> {2,3}      num >> 1,2得1，  {nums[1],nums[2]}
            111  -> {1,2,3}    num >> 0,1,2得1，{nums[0],nums[1],nums[2]}
"""


class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)
        for i in range(2 ** n):
            sub = []  # 清空上一轮的结果
            for j in range(n):
                if i >> j & 1:
                    sub.append(nums[j])
            res.append(sub)
        return res


"""
    解题思路2：
        如何用深搜来解决此问题呢？
        
        按照前面思路，我们同样是依次枚举集合中的每一个元素，每个元素有两种可能，加入 或者 不加入 到当前集合中
        
        我用一个for循环实现上面目标，i=0时，添加空集，i=1时添加元素入集合
"""


class Solution2:
    res = []
    sub = []

    def subsets(self, nums):
        if not nums:
            return []
        self.res = []
        self.sub = []
        self.dfs(nums, 0)
        return self.res

    def dfs(self, nums, idx):
        if idx == len(nums):
            self.res.append(self.sub.copy())
            return
        for i in range(2):
            if i == 0:
                self.dfs(nums, idx + 1)  # 不做处理，直接dfs下一个元素
            else:
                self.sub.append(nums[idx])  # 添加当前元素到集合中
                self.dfs(nums, idx + 1)
                self.sub.pop()  # 回溯过程，弹出插入的元素


if __name__ == '__main__':
    print(Solution().subsets([1, 2, 3]))
    print(Solution2().subsets([1, 2, 3]))
