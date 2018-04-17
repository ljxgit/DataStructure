# -*- coding:utf-8 -*-
# 选择排序有两种：1、直接选择排序 2、堆排序
# 直接选择排序：一种不稳定的排序，时间复杂度都是O(n^2)
# 一种简单的、直观的排序方法，每一次找出n个、n-1个....1个数中最小的元素，放在数组最前列，最后组成由小到大的有序数组
def select_sort(arr):
    for i in range(len(arr)): # 时间复杂度O(n^2)
        min = arr[i]
        idx = i # 保存最小值的索引
        for j in range(i+1,len(arr)):
            if arr[j]<min: # 如果有更小的，交换
                min = arr[j]
                idx = j
        arr[idx] = arr[i]
        arr[i] = min # 把最小的元素放在数组最前面，最终构成有序数组
