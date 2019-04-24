# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/23/19 1:19 PM
 @desc: 给定一组非负整数组成的数组h，代表一组柱状图的高度，其中每个柱子的宽度都为1。 在这组柱状图中找到能组成的最大矩形的面积
        入参h为一个整型数组，代表每个柱子的高度，返回面积的值
"""
"""
 输入描述:
    输入包括两行,第一行包含一个整数n(1 ≤ n ≤ 10000)
    第二行包括n个整数,表示h数组中的每个值,h_i(1 ≤ h_i ≤ 1,000,000)
    
 输出描述:
    输出一个整数,表示最大的矩阵面积
    
 输入例子:
    6
    2 1 5 6 2 3

 输出例子:
    10
"""

"""
 有一个可以肯定的结论：
    组成矩形的最大面积时，必有某一个柱子的高度等于矩形的高度!
    
 那我们想办法统计每一个柱子为矩形最大高度时，所能组成的矩形的最大面积!
"""


# 这里给出两种解决办法

class Solution:
    # 法一：枚举法，暴力搜索,针对每一个bar,分别从左到右扫描出满足条件的最左的bar的下标和最右的bar的下标，此方法在牛客网上运行通过
    # 时间复杂度是O(n^2)，空间复杂度为O(1)，这种算法思想比较好理解
    def max_area_1(self, length, heights):
        max_area = 0
        for i in range(length):
            left = right = i  # 一定要先初始化left和right的值，然后在判断left和right是否可以向左或者向右移动
            # 向左开始扫描
            for j in range(i, -1, -1):
                if heights[j] >= heights[i]:
                    left = j
                else:
                    break
            # 向右开始扫描
            for k in range(i + 1, length):
                if heights[k] >= heights[i]:
                    right = k
                else:
                    break
            area = heights[i] * (right - left + 1)
            max_area = max(area, max_area)
        return max_area

    # 法二：维护一个单调递增的栈，栈里面存储的是元素的索引值，详情参考https://blog.csdn.net/qq_17550379/article/details/85093224

    # 下面针对具体例子heights = [6,2,5,4,5,1,6]，进行分析：
    # i=0<length=7，进入if判断，由于栈为空，条件不成立，i入栈，stack=[0]，i=1

    # i=1<length=7，进入if判断，栈不为空，并且6>2，条件成立，pop栈顶元素，此时栈为空，width=i=1，max_area=max(0,6)=6
    # 下一轮while循环，i=1<7，进入if判断，栈为空，if不成立，i入栈，stack=[1]，i=2

    # i=2<length=7，进入if判断，栈不为空，但是2<5，if不成立，i入栈，stack=[1,2]，i=3

    # i=3<length=7，进入if判断，栈不为空，并且4>5，if成立，pop栈顶元素，栈为[1]不为空，width=3-stack[-1]-1=1,max_area=max(4,6)=6
    # 下一轮while循环，i=3<7，进入if判断，栈不为空，但是2<4，if不成立，i入栈，stack=[1,3]，i=4

    # i=4<length=7，进入if判断，栈不为空，但是4<5，if不成立，i入栈，stack=[1,3,4]，i=5

    # i=5<length=7，进入if判断，栈不为空，并且5>1，if成立，pop栈顶元素，栈为[1,3]不为空，width=5-stack[-1]-1=1,max_area=max(6,6)=6
    # 下一轮while循环，i=5<7，进入if判断，栈不为空，且4>1，if成立，pop，栈为[1]不为空，width=5-stack[-1]-1=3,max_area=max(12,6)=12
    # 下一轮while循环，i=5<7，进入if判断，栈不为空，且2>1，if成立，pop，栈为[]为空，width=5,max_area=max(10,12)=12
    # 下一轮while循环，i=5<7，进入if判断，栈为空，if不成立，i入栈，stack=[5]，i=6

    # i=6<length=7，进入if判断，栈不为空，但是1<6，if不成立，i入栈，stack=[5,6]，i=7

    # i=7<length=7不成立，while循环结束

    # 下面的while循环开始
    # stack=[5,6]不为空，pop，此时stack=[5]，width = 7 - stack[-1] -1 = 1，max_area=max(6,12)=12
    # stack=[5]不为空，pop，此时stack=[]为空，width = 7，max_area=max(7,12)=12
    # stack=[]为空，while结束，返回最终的max_area=12

    def max_area_2(self, length, heights):
        stack = []
        max_area = 0
        i = 0
        while i < length:
            if stack and heights[stack[-1]] > heights[i]:
                top_idx = stack.pop()
                # 注意：空列表也是一个list对象，不为None！因此判断空列表用 len(a)==0，而不能用 a is None ！！！！！！！！！
                # 但是空的列表a，可以表示False！
                width = i if len(stack) == 0 else (i - stack[-1] - 1)
                area = heights[top_idx] * width
                max_area = max(area, max_area)
            else:
                stack.append(i)
                i += 1
        while stack:
            top_idx = stack.pop()
            width = i if len(stack) == 0 else (i - stack[-1] - 1)
            area = heights[top_idx] * width
            max_area = max(area, max_area)
        return max_area


if __name__ == "__main__":
    sol = Solution()
    input_length = int(input())
    input_heights = [int(x) for x in input().split()]
    print(sol.max_area_1(input_length, input_heights))
    print(sol.max_area_2(input_length, input_heights))
