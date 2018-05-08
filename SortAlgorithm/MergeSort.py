# -*- coding:utf-8 -*-
# Python实现归并排序（稳定排序），主要思想是合并两个有序数组，如果是一个无序的数组，则首先拆分成单个元素，然后两两合并成有序数组，时间复杂度是O(nlogn)
def merge_sort(lists):
    # 递归，先拆分，再合并
    if len(lists) <= 1:
        return lists
    mid = len(lists)>>1
    # 切分到left和right都只有一个元素时，开始合并
    left = merge_sort(lists[:mid])
    right = merge_sort(lists[mid:])
    return merge(left, right)

# 合并两个列表，left和right各自已经是有序数组
def merge(left,right):
    result = []
    idx1 = idx2 =0
    while(idx1<len(left) and idx2<len(right)):
        if left[idx1]<right[idx2]:
            result.append(left[idx1])
            idx1+=1
        else:
            result.append(right[idx2])
            idx2+=1
    if idx1<len(left): # left有剩余元素，直接加入result列表
        result.extend(left[idx1:])
    if idx2<len(right):
        result.extend(right[idx2:])
    return result
