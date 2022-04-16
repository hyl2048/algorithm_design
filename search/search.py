

def binary_search(arr, start, end, target):# 二分法 递归
    mid = int(( start + end ) / 2)
    if (start > end):
        return -1
    if (arr[mid] == target):
        return mid
    if(arr[mid] < target):
        return binary_search(arr, mid + 1, end, target)
    return  binary_search(arr, start, mid -1, target)

def binary_search(arr, target):# 二分法 非递归
    if len(arr) == 0 or arr == None:
        return -1
    start = 0
    end = len(arr) - 1
    while(start < end):
        mid = int((start + end) / 2)
        if (arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            start = mid + 1
        else:
            end = mid - 1
    if (arr[start] == target):# 判断 不等于中间值的情况
        return start
    return -1

def binary_search2(arr, target):# 二分法 非递归 进阶版
    if len(arr) == 0 or arr == None:
        return -1
    start = 0
    end = len(arr) - 1
    while(start + 1 < end): # 在剩余最后两个数的时候退出来 防止死循环
        mid = int(start + (end - start ) / 2)
        if (arr[mid] == target):
            return mid
        elif(arr[mid] < target):
            start = mid
        else:
            end = mid
    if (arr[end] == target):
        return end
    if (arr[start] == target):# 判断 不等于中间值的情况
        return start
    return -1
            
if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    
    print(binary_search2(arr, 9))