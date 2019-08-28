# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 13:47
 @desc: 第216题
        找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。
        说明：
            所有数字都是正整数。
            解集不能包含重复的组合。
"""


class Solution:
    res = []
    path = []
    k = 0

    def combinationSum3(self, k: int, n: int):
        if not k or not n:
            return []
        self.res = []
        self.path = []
        self.k = k
        self.dfs(0, 1, n)
        return self.res

    def dfs(self, idx, num, target):
        """
        :param idx: 当前path的元素个数为idx
        :param num: 当前待添加到path中的数字
        :param target: 本轮数字填充到path中中，剩余需要拼凑的值
        :return:
        """
        if idx == self.k and target == 0:
            self.res.append(self.path.copy())
            return
        for i in range(num, 10):
            self.path.append(i)
            if target - i >= 0:  # 条件不成立时，没必要向下搜索
                self.dfs(idx + 1, i + 1, target - i)
            self.path.pop()


if __name__ == '__main__':
    print(Solution().combinationSum3(3, 12))
