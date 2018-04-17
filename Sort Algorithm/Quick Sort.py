# -*- coding:utf-8 -*-
# 快速排序：一种不稳定的基于交换的排序算法，最坏时间复杂度为O(n^2)，最好和平均都是O(nlogn)，相比冒泡排序，每一次的交换是跳跃的，不是相邻元素交换，并且使用了分治法
# 通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
# 然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。
def quick_sort(arr,start,end):
    # 定义两个游标，分别从左到右、从右到左遍历数组
    if start >= end:
        return arr
    i = start
    j = end
    base = arr[start] # 选取第一个元素作为基准
    while(i!=j):
        while(arr[j]>=base and j>i): # 从后向前遍历，找到比基准小的元素，停下
            j-=1
        while(arr[i]<=base and i<j): # 从前向后遍历，找到比基准大的元素，停下
            i+=1
        if(i<j): # 交换
            arr[i], arr[j] = arr[j], arr[i]
    arr[start] = arr[i] # 如果i=j，代表此次探测完成，将基准元素放置在i处，即序列大小中间处
    arr[i] = base
    # 分治法，递归实现
    quick_sort(arr,start,i-1) # 将基准左边排成一个有序序列
    quick_sort(arr,i+1,end) # 将基准右边排成一个有序序列
    return arr

a=[1,2,3,4,5]
print(quick_sort(a,0,4))