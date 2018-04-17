# -*- coding:utf-8 -*-
# 交换排序有两种：1、冒泡排序 2、快速排序
# 冒泡排序：一种稳定的排序算法，最好时间复杂度为O(n)，最坏和平均都是O(n^2)
# 比较相邻元素，如果不符合排序，则交换。一次找出n、n-1、n-2....1个数字中最小的，按照从小到大顺序排列
def bubble_sort(arr):
    for i in range(0,len(arr)-1): # 固定一个游标
        for j in range(i+1,len(arr)): # 另一个游标遍历，寻找不符合排序的元素
            if arr[j]<arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr

a=[2,56,1,0,33,11,4]
print(bubble_sort(a))
