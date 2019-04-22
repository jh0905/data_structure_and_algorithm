# encoding: utf-8
"""
 @project:data_structure_and_algorithm
 @author: Jiang Hui
 @language:Python 3.7.2 [GCC 7.3.0] :: Anaconda, Inc. on linux
 @time: 4/22/19 9:45 AM
 @desc:二分查找法，要求元素必须是有序的，如果是无序的，则要先进行排序操作!
"""
"""
 1.基本思想：
 
    也称为折半查找法，属于有序查找算法，用给定值k先与中间节点的关键字比较，中间节点把线性表分成两个子表，若相等，则查找成功若不相等，再根据k与
 中间节点的关键字的大小，确定下一步找哪个子表，递归进行下去
 
 2.复杂度分析：
 
    最坏情况下，关键字比较次数为log n,且时间复杂度为O(log n)，这里的log都是以2为底
    
 3.应用场景：
    
    折半查找的前提条件是需要有序表顺序存储，对于静态查找表，一次排序后不再变化，折半查找能得到不错的效率。但对于需要频繁执行插入或删除操作的
 数据集来说，维护有序的排序会带来不小的工作量，那就不建议使用。   ----《大话数据结构》
                                                        
"""


# 非递归版本
# 注意几个点：
# 一是while循环条件是low<=high
# 二是如果nums[mid]<key，low = mid + 1
#    如果nums[mid]>key，high = mid - 1
# 之所以用加1减1，是因为我们第一判断nums[mid] == key，如果不是的话，那mid这个元素在下一轮就无意义了，另外如果不去掉的话，程序会陷入死循环
def binary_search_1(nums, key):
    length = len(nums)
    low = 0
    high = length - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


# 递归版本的实现，有几个要注意的地方
# 一是：递归停止条件有两个，一个是找到了元素的情况，另外一个是找不到元素情况
# 二是：同上面一样，如果nums[mid]不等于当前值，那么我们在下一轮中要剔除这个值
# 三是：这里的递归，在调用方法前，加上return，不然的话，只会返回到该函数上一层的调用，因此一定要记得加上return
def binary_search_2(nums, key, low, high):
    mid = (low + high) // 2
    if low == high and nums[low] != key:
        return -1
    if nums[mid] == key:
        return mid
    elif nums[mid] < key:
        return binary_search_2(nums, key, mid + 1, high)
    else:
        return binary_search_2(nums, key, low, mid - 1)


# 这里再引申一个算法，如果原数组为旋转数组如[5,6,7,8,9,1,2,3,4]，那么如何用O(log n)的时间复杂度查找到某个元素
# 算法思路：
#   while循环条件仍然是 low<=high
#       mid = (low+high)//2
#       如果nums[mid]==key，则返回mid
#       重点来了，这里判断nums[mid]与nums[low]谁比较大，如果nums[mid]更大，说明左边有序，判断key是否在左边区间内，调整low和high的值
#       如果nums[low]大于nums[mid]，那么说明右边有序，判断key是否处于右边区间，调整相应的low和high的值
#       while循环结束，程序还没有返回，那么返回-1
def bin_search(nums, key):
    length = len(nums)
    low = 0
    high = length - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == key:
            return mid
        elif nums[mid] > nums[low]:  # 左边有序，右边无序
            if nums[low] <= key < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:  # 左边无序，右边有序
            if nums[mid] < key <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1


if __name__ == '__main__':
    search_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    search_key = 6
    print(binary_search_1(search_nums, search_key))
    print(binary_search_2(search_nums, search_key, 0, len(search_nums) - 1))
    rotate_nums = [7, 8, 9, 1, 2, 3, 4, 5, 6]
    print(bin_search(rotate_nums, search_key))
