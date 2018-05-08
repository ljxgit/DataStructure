# # -*- coding:utf-8 -*-
"""
利用Python构建一个堆，使用数组存储，定义建立堆、调整堆、维护堆（pop&push）等方法，实现堆排序、topK等应用
堆heap是一个特殊的完全二叉树，其任意结点始终不大于（不小于）其左右子结点，分别为小顶堆、大顶堆，由于完全二叉树存储效率高，不浪费空间，
所以一般用数组来描述一个堆，直接采用下标索引每个结点，节省了子结点指针空间，父结点下标为i，则其左右子结点下标分别为2*i+1、2*i+2
大顶堆：arr[i] >= arr[2i+1] && arr[i] >= arr[2i+2]
小顶堆：arr[i] <= arr[2i+1] && arr[i] <= arr[2i+2]
"""
# 定义构建大顶堆的方法，直接在数组arr[]上就地堆化，1、向上调整 2、向下调整
# 向上调整构建堆（上滤），从叶节点入手，逐个向上比较
def heap_create_up(arr):
    n = len(arr)
    for i in range(1,n): # 每一个元素调整一次O(logn)，共n个元素，所以堆化（创建堆）时间复杂度O(nlogn)
        heap_adjust_up(arr,i) # 从第二个元素开始遍历，每一次都重新调整一次堆

def heap_adjust_up(arr,i): # 向上调整堆，时间复杂度O(logn)
    p = int((i-1)/2) # 父结点的下标，长度为n的数组，最后一个父结点为n/2-1
    while(arr[p]<arr[i]): # 如果父结点小于当前结点
        temp = arr[i] # 交换子结点与父结点的值，直到父结点大于子结点，符合大顶堆性质
        arr[i] = arr[p]
        arr[p] = temp
        i = p
        p = int((i-1)/2)

# 向下调整构建堆（下滤），从父节点入手，与其左右子结点比较
def heap_create_down(arr):
    n = len(arr)
    for i in range((n>>1)-1,-1,-1):
        heap_adjust_down(arr,i,n) # 从最后一个非叶节点开始遍历，直到根结点，每一次都重新调整一次堆

def heap_adjust_down(arr,i,n): # 向下调整堆，从最后一个父结点入手，与其左右子结点比较。调整一次时间复杂度为O(logn)
    max = i # 记录最大值的下标
    while(i<(n>>1)): # 保证i是非叶节点的下标
        if (2*i+1<n and arr[2*i+1]>arr[max]): # 左结点大于当前父结点
            max = 2*i+1
        if (2*i+2<n and arr[2*i+2]>arr[max]): # 右结点结点大于当前最大值
            max = 2*i+2
        if max == i: # 当前父结点最大
            break
        temp = arr[max]
        arr[max] = arr[i]
        arr[i] = temp
        i = max # 将子结点作为当前父结点继续迭代

# 堆的维护，主要包括插入和删除两个操作，由于堆是一个优先级队列，插入元素只能在数组尾部，删除元素只能在堆顶（数组第一个元素）
# 新元素插入堆中，数组末尾
def heap_push(arr, val):
    arr.append(val) # 插入数组
    heap_adjust_up(arr,len(arr)-1) # 重新调整堆，采用向上调整
    return arr
# 删除堆元素，堆只能删除堆顶元素，数组第一个
def heap_pop(arr):
    temp = arr[-1]
    arr[-1] = arr[0]
    arr[0] = temp
    arr = arr[:len(arr)-1] # 删除最后一个元素
    heap_adjust_down(arr,0,len(arr)) # 从根结点开始，向下调整
    return arr

# 堆排序，一种不稳定的选择排序，最好、平均、最坏时间复杂度均为O(nlogn)，直接在原数组中就地排序，无需额外的存储空间，一般采用向下调整的方法，调整根结点
# 1、堆化，将数组建立为一个大顶堆（小顶堆）
# 2、排序，调整堆，每次将堆尾元素（数组末尾元素）与堆顶元素交换，最大的放在数组末尾，然后重新调整堆，获得次大的值，直到最后只剩一个最小的结点
def heap_sort(arr):
    n = len(arr) # 数组长度
    # 首先对数组堆化，将其变为大顶堆，时间复杂度O(nlogn)
    heap_create_down(arr)
    # 堆排序，交换堆顶元素与最后一个元素，然后调整堆，时间复杂度O(nlogn)
    for i in range(n-1,0,-1):
        arr[0], arr[i] = arr[i], arr[0]
        heap_adjust_down(arr,0,i)

# Top k问题，在N个无序元素中，找到最大的k个元素，可以借助堆排序，先构建一个含有k元素的小顶堆，然后从arr[k+1]开始遍历，如果比堆顶大，则替换堆顶，
# 然后重新调整堆，最后得到最大的k个元素。建堆的时间复杂度为O(klogk)，寻找最小的k个元素时间复杂为O((N-k)logk)，总时间复杂度为O(Nlogk)
def topk(arr,k):
    res = arr[:k] # 取原数组的前k个元素
    heap_create_down(res) # 堆化k个元素，大顶堆
    for i in range(k,len(arr)):
        if arr[i] < res[0]: # 如果小于堆顶
            res[0] = arr[i] # 交换
            heap_adjust_down(res,0,k) # 调整含有k个元素的堆，使其重新成为大顶堆
    return res

a = [1,5,3,7,2,9,6,88,22,567]
heap_create_down(a)
heap_sort(a)
print(a)