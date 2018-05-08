# -*- coding:utf-8 -*-
# 希尔排序：
def Shell_sort(arr): # 基于移动元素实现的希尔排序
    # 首先定义增量，从len/2开始直至减为1
    gap = len(arr)>>1
    while(gap>0):
        for i in range(gap,len(arr)): # 对每个组内类似直接插入排序
            new = arr[i]
            j = i
            if arr[j-gap]>new: # 与插入排序原理相同，如果前面元素大于新元素，则移动
                while(j>=gap and arr[j-gap]>new):
                    arr[j] = arr[j-gap] # 基于移动的，没有交换
                    j -= gap
                arr[j] = new
        gap = gap>>1
    return arr

def Shell_sort_swap(arr): # 基于交换元素实现的希尔排序
    # 首先定义增量，从len/2开始直至减为1
    gap = len(arr)>>1
    while(gap>0):
        for i in range(gap,len(arr)): # 对每个组内类似直接插入排序
            j = i
            while(j>=gap and arr[j-gap]>arr[j]): # 如果前面元素大于新元素，则交换
                arr[j], arr[j-gap] = arr[j-gap],arr[j]
                j -= gap
        gap = gap>>1
    return arr

a=[34,8,64,51,32,21]
print(Shell_sort_swap(a))