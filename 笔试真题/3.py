# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/24 15:59
 @desc:
"""
if __name__ == '__main__':
    c = int(input())
    for i in range(c):
        nums = list(map(int, input().split()))
        n = nums.pop(0)  # 弹出角色个数
        if n < 3:
            print(0)
        else:
            res = 0
            nums = sorted(nums, reverse=True)
            while len(nums) >= 3:
                print(nums)
                res += nums[2]
                for j in range(3):
                    nums[j] -= nums[2]
                nums.pop(2)
                nums = sorted(nums, reverse=True)
            print(res)
