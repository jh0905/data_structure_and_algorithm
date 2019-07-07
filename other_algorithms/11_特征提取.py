# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 7/7/19 4:25 PM
 @desc:
"""
# 接收输入，存储所有帧的信息
M = int(input())
frames = []
while M:
    frame = [int(x) for x in input().strip().split()]
    n = frame.pop(0)  # 提取出特征总数
    features = []  # 储存特征对
    for i in range(n):
        # 注意，我们这里把特征对存储为tuple形式，是为了之后让它作为dict的键，list不能作为键
        features.append(tuple(frame[2 * i: 2 * i + 2]))
    frames.append(features)
    M -= 1
# 当前帧是一定有该特征的，故初始长度为1，我们从当前层的上一帧开始查找
max_length = length = 1
for i in range(len(frames)):  # 第一层：从上到下，遍历每一帧
    for j in range(len(frames[i])):  # 第二层：遍历每一帧的每一个特征对
        for k in range(i - 1, -1, -1):  # 第三层：从当前帧的上一帧，往上查找
            if frames[i][j] in frames[k]:  # 第四层：判断当前特征是否在该帧出现
                length += 1
            else:
                break  # 退出第三层循环
        max_length = max(max_length, length)
        length = 1  # 退出第三层循环时，要把length重置为1
print(max_length)

max_length = 0
last_time = dict()
count = dict()  # 初始化两个字典变量
for i in range(len(frames)):  # 第一层：从上到下，遍历每一帧
    for j in range(len(frames[i])):  # 第二层：遍历每一帧的每一个特征对
        feature_pair = frames[i][j]
        if feature_pair not in last_time:  # 如果当前特征第一次出现
            count[feature_pair] = 1
        elif last_time[feature_pair] == i - 1:  # 当前特征在上一帧中出现
            count[feature_pair] += 1
        elif last_time[feature_pair] < i - 1:  # 如果同一个帧中有两个相同的特征，则会出现last_time[feature_pair] == i > i-1
            count[feature_pair] = 1
        max_length = max(max_length, count[feature_pair])
        last_time[feature_pair] = i
print(max_length)
