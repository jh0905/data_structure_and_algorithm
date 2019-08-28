# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 2019/8/28 10:57
 @desc: 第76题

        给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

        输入: S = "ADOBECODEBANC", T = "ABC"
        输出: "BANC"
"""
"""
    本题是经典的滑动窗口试题，不妨把本题的解法，用作以后滑动窗口问题的代码模板！
    
    step1: 定义两个哈希表，needs用来存储target中的元素个数，window用来统计窗口内所包含的各个元素的个数。
    
    step2: 如果window中，新加入的某个元素是target中的元素，并且它在window中的个数 == target中的个数，match+=1
    
    step3: r += 1 ,window更新完某个key的值之后，把r指针右移一位
    
    step4: while match == len(needs): 说明窗口内已经涵盖了target中的元素个数，我们判断l指针，是否可以右移
           缩小窗口大小，但是要保证窗口内要始终包含target里的所有元素
           if s[l] not in needs: 说明l指向的元素无用，直接右移，并continue
           if windows[s[l]] > needs[s[l]] 说明l指向的元素冗余，可以去掉，右移一位，并continue
           前两个if如果都没执行，说明到这里l已经不能再移动了，
           我们再判断此时的区间，是否小于当前最小的子串。是的话，覆盖并break
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mins = ''
        needs, window = {}, {}
        for ch in t:
            needs[ch] = needs.get(ch, 0) + 1
        l, r = 0, 0
        match = 0  # 记录窗口中有多少个满足数量的字符
        while r < len(s):
            window[s[r]] = window.get(s[r], 0) + 1
            if s[r] in needs and window[s[r]] == needs[s[r]]:
                match += 1
            r += 1  # r 指针右移1位
            while match == len(needs):  # 判断l指针是否需要移动
                if s[l] not in needs:  # 当前元素不属于指定元素，l直接右移1位，并continue
                    l += 1
                    continue
                if window[s[l]] > needs[s[l]]:  # 当前元素属于指定元素，并且数量存在冗余，则l右移1位，并continue
                    window[s[l]] -= 1
                    l += 1
                    continue
                if not mins or len(mins) > r - l:  # 到达这里，说明l位置不能再移动，否则无法满足题目要求
                    mins = s[l:r]
                break
        return mins


if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s, t))
