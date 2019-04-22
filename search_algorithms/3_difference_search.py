# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 1:48 PM
 @desc:差值查找法，二分查找的改进
"""
import math

"""
 引子：
    打个比方，在英文字典里面查“apple”，你下意识翻开字典是翻前面的书页还是后面的书页呢？如果再让你查“zoo”，你又怎么查？很显然，这里你绝对不会
 是从中间开始查起，而是有一定目的的往前或往后翻。同样的，比如要在取值范围1 ~ 10000 之间 100 个元素从小到大均匀分布的数组中查找5， 我们自然会
 考虑从数组下标较小的开始查找。经过以上分析，折半查找这种查找方式，不是自适应的（也就是说是傻瓜式的）
    
    二分查找的查找点计算方式为： mid = (low+high)//2 或者 mid = low + 1/2 *(high-low)
    以此类推，差值查找的查找点计算为： mid = low + (key - nums[low])/(nums[high]-nums[low]) * (high-low)
    也就是说，将上述的比例参数从1/2改进为自适应的，根据关键字在整个有序数组中的位置，让mid的位置更接近于关键字key
 
 1.基本思想：
    基于【二分查找】算法，将查找点的选择改进为自适应选择，可以提高查找效率，同样是基于有序数组   
 
 2.复杂度分析：
    查找成功或者失败的时间复杂度均为O(log log n)，log均是以2为底
    
 3.适用场景：
    对于表长将大，而元素分布比较均匀的查找表来说，差值查找的平均性能比折半查找好得多，反之，如果元素分布非常不均匀(相邻元素之间的差值起伏大)
 那么差值查找未必是很合适的选择.
"""


def difference_search(nums, key, low, high):
    # 这一步要放在计算mid之前，避免出现除数为0的异常情况
    if low == high and nums[low] != key:
        return -1
    # math.floor()为向下取整，math.ceil()为向上取整，math.round()为四舍五入
    mid = math.floor(low + (key - nums[low]) / (nums[high] - nums[low]) * (high - low))
    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return difference_search(nums, key, low + 1, high)
    else:
        return difference_search(nums, key, low, high - 1)


if __name__ == '__main__':
    search_nums = [1, 3, 4, 5, 7, 9, 11, 13]
    search_key = 12
    print(difference_search(search_nums, search_key, 0, len(search_nums) - 1))
