# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/29 19:47
 @desc: 远景
"""
if __name__ == '__main__':
    d = list(map(int, input().split()))  # 距离数组
    nums = list(map(int, input().split()))  # 发电量数组
    n = int(input())  # 输电总距离限制
    dic = []
    for i in range(len(d)):
        dic.append([d[i],nums[i]])
    dic = sorted(dic, reverse=True)
    for i in range(len(dic)):
        d[i] = dic[i][0]
        nums[i] = dic[i][1]
    # 距离之和小于限制值时的最大值
    ans = 0
    for i in range(len(d)):
        if d[i] > n:
            continue
        cnt = d[i]
        v = nums[i]
        for j in range(i + 1, len(d)):
            if cnt + d[j] > n:
                ans = max(ans, v)
                break
            cnt += d[j]
            v += nums[j]
        ans = max(ans, v)
    print(ans)
