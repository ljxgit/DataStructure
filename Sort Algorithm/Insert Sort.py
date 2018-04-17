# -*- coding:utf-8 -*-
# 插入排序有两种：1、直接插入排序 2、希尔排序
# 直接插入排序：一种稳定的基于比较的排序，这种排序有两种基本操作：1、比较 2、交换
# 插入排序有N-1趟排序组成，可以用递归实现，平均时间复杂度是O(n^2)，最好的是O(n)
# 最好的情况就是本来就是有序数组，只需要遍历一遍，没有交换操作，所以是O(n)
# 平均情况就是每遍历一个元素，都要和前面的元素有交换操作，所以是O(n^2)
def insert_sort(arr):
    for i in range(1,len(arr)): # arr[:i-1]已经是有序序列
        new = arr[i] # 新插入元素
        for j in range(i,0,-1): #和之前的的i-1个元素一一对比
            if arr[j-1]>new: # 如果第i-1元素大于新元素，则交换，也可以利用移动来实现，不交换
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
            else: # 否则，前面i-1个元素都小于新元素，已经是有序序列
                break
    return arr

def insert_sort_move(arr):
    for i in range(1,len(arr)): # arr[:i-1]已经是有序序列
        new = arr[i] # 新插入元素
        j = i
        if arr[j-1]>new:
            while(j>=1 and arr[j-1]>new): # 如果前面有元素大于新插入元素，则将其向后移动一位
                arr[j] = arr[j-1] # 只是移动元素，并没有交换
                j -= 1
            arr[j] = new # 最后将新插入元素放置在j处
    return arr

a=[34,8,64,51,32,21]
print(insert_sort_move(a))