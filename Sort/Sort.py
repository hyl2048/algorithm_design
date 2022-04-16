

def bubble_sort(arr): #比较 冒泡
    length = len(arr)
    for i in range(length):
        for j in range(0,length-i-1):
              if arr[j] < arr[j+1]:
                  arr[j], arr[j+1] = arr[j+1], arr[j]
            # print(i)
    return arr

def quick_sort(arr):# 快排 分治法 递归  1函数功能 2停止条件 3递归函数
    if not len(arr):
        return []
    else:
        pivot = arr[0]
        left = quick_sort([x for x in arr[1:] if x >= pivot])
        right = quick_sort([x for x in arr[1:] if x < pivot])
    return left + [pivot] + right

def quick_sort_stack(arr):# 快排 分治法 栈
    if len(arr) < 2:
        return arr
    stack = []
    stack.append(len(arr) - 1)
    stack.append(0)
    while stack:# 用栈来存储双指针位置，各个分区终始点
        l = stack.pop()
        r = stack.pop()
        index = partition(arr, l, r )
        if l < index - 1:
            stack.append(index -1)
            stack.append(l)
        if r > index + 1:
            stack.append(r)
            stack.append(index + 1)
    return  arr
def partition(arr, start, end):
    pivot = arr[start]
    while start < end:
        while start < end and arr[end] >= pivot:
            end -= 1
        arr[start] = arr[end]
        while start < end and arr[start] <= pivot:
            start += 1
    arr[start] = pivot
    return start

def merge_sort(arr, l, r):
    if l < r:
        m = int((l + (r - 1))/2)
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)
    # return arr

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = arr[l + i]
    
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        
    i = 0
    j = 0
    k = l
    
    while i < n1 and j< n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# def merge(arr, l, m, r):
#     n1 = m - l + 1
#     n2 = r - m
#
#     # 创建临时数组
#     L = [0] * (n1)
#     R = [0] * (n2)
#
#     # 拷贝数据到临时数组 arrays L[] 和 R[]
#     for i in range(0, n1):
#         L[i] = arr[l + i]
#
#     for j in range(0, n2):
#         R[j] = arr[m + 1 + j]
#
#         # 归并临时数组到 arr[l..r]
#     i = 0  # 初始化第一个子数组的索引
#     j = 0  # 初始化第二个子数组的索引
#     k = l  # 初始归并子数组的索引
#
#     while i < n1 and j < n2:
#         if L[i] <= R[j]:
#             arr[k] = L[i]
#             i += 1
#         else:
#             arr[k] = R[j]
#             j += 1
#         k += 1
#
#     # 拷贝 L[] 的保留元素
#     while i < n1:
#         arr[k] = L[i]
#         i += 1
#         k += 1
#
#     # 拷贝 R[] 的保留元素
#     while j < n2:
#         arr[k] = R[j]
#         j += 1
#         k += 1
#
#
# def mergeSort(arr, l, r):
#     if l < r:
#         m = int((l + (r - 1)) / 2)
#
#         mergeSort(arr, l, m)
#         mergeSort(arr, m + 1, r)
#         merge(arr, l, m, r)



if __name__ == '__main__':
    arr =[11,2,5,6,9]
    # arr_sort = bubble_sort(arr)
    # arr_sort = quick_sort(arr)
    # arr_sort = quick_sort_stack(arr)
    merge_sort(arr, 0, len(arr)-1)
    for i in arr:
        print(i)
        
# 参考 https://www.cnblogs.com/zhousong918/p/10172343.html