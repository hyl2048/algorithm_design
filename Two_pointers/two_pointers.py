
#背向指针
def expendcenter(str, left, right):
    while left >= 0 and  right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1
    return left + 1, right - 1
def longest_palindromic_substring(str): #最长回文子串
    if len(str) == 1:
        return str
    start = 0
    end = 0
    for i in range(len(str)):
        left1, right1 = expendcenter(str, i, i)
        left2, right2 = expendcenter(str, i, i+1)
        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end -start:
            start, end = left2, right2
    return str[start:end + 1]
            
def find_k_closed_elements(arr, k, x): # k个最近的元素
    ans =[]
    if arr[0] <= x <= arr[len(arr)-1]:
        xindex = getxindex(arr,x)
        left = max(0, xindex - k -1)
        right = min(len(arr) - 1, xindex + k - 1)
        while (right - left > k -1) :
           if (x - arr[left] <= arr[right] - x):
               right -= 1
           elif(x - arr[left] > arr[right] - x):
               left += 1
           else:
               print('unhandled case:' + left +''+right)
        ans = arr[left : right + 1]
            
        
    elif(arr[0] > x):
        for i in range(0,k):
            ans.append(arr[i])
    else:
        for i in range(k,len(arr)):
            ans.append(arr[i])
    return ans

def getxindex(arr, x):
    for i in range(len(arr)):
        if arr[i] < x:
            continue
        else:
            return i
# 同向指针
def longest_substr_NoRep(str):# sliding window 无重复最长子串
    left = 0
    right = -1
    wind = set()
    n = len(str)
    ans = 0
    for i in range(n):
        if i != 0:
            wind.remove(str[i - 1])  # 在第一个重复区域第一个位置停下并逐个移除wind中的值
        while right + 1 < n and str[right + 1] not in wind:
            wind.add(str[right + 1])
            right += 1
        ans = max(ans, right - i + 1)
    return ans
#同向指针 fast and slow pointer
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None
class SLinkedList:
    def __init__(self):
        self.headval = None
def creatLinkNode(n):
    head = Node(0)
    first = head
    for i in range(1,n):
        first.nextval = Node(i)
        first = first.nextval
    return head

def creatLinkNode_with_cycle(cycle_start,n):
    head = Node(0)
    first = head
    second = head
    for i in range(1, n):
        first.nextval = Node(i)
        first = first.nextval
    for i in range(0,cycle_start):
        second = second.nextval
    first.nextval = second
    return head
def printLinkNode(head):
    second = head
    while True:
        print(second.dataval)
        second = second.nextval
        if second.nextval == None:# 边界处理
            print(second.dataval)
            break
def f_mid_point_link(head):
    first = head
    second = head
    while True:
        first = first.nextval
        second = second.nextval.nextval
        if   second == None or second.nextval == None:
            return first.dataval

def find_cycle_linkNode(head):
    first = head
    second = head
    while True:
        first = first.nextval
        second = second.nextval.nextval
        if first.dataval == second.dataval:
            return True
        elif second == None or second.nextval == None:
            return False

def find_cycle_entra(head):
    first = head
    second = head
    while True:
        first = first.nextval
        second = second.nextval.nextval
        if first.dataval == second.dataval:
            break
        elif second == None or second.nextval == None:
            return False
    third = head
    while first.dataval != third.dataval:
        first = first.nextval
        third = third.nextval
    return third.dataval
# 相向指针 two sum;
def find_two_sum(arr, target):
    start = 0
    
    for i in range(0, len(arr)):
        val = target - arr[i]
        end = len(arr) - 1
        while  val >= 0:
            if arr[end] == val:
                return i, end
            end -= 1

def find_two_sum_v2(arr, target):#
    temp = dict()
    for i in range(0, len(arr) - 1):
        if target - arr[i] in temp:
            return temp[target - arr[i]], i
        temp[arr[i]] = i
    return []

def sort(arr):
    if not len(arr):
       return []
    else:
       pivot = arr[0]
       left = sort([x for x in arr[1:] if x < pivot])
       right = sort([x for x in arr[1:] if x >= pivot])
    return  left + [pivot] + right
    

def find_two_sum_v3(arr, target):
    arr =  sort(arr)
    for i in range(len(arr)):
        print(arr[i])
    start = 0
    end = len(arr) - 1
    for i in range(0,len(arr)):
        if arr[start] + arr[end] == target:
            return start , end
        elif(arr[start] + arr[end] < target):
            start += 1
        else:
            end -= 1

def find_two_sum_v4(arr, target):# 相向双指针
    left = 0
    right = len(arr) - 1
    temp = dict()
    while left < right:
        tarL = target - arr[left]
        tarR = target - arr[right]
        if (tarL in temp):
            return left, temp[tarL]
        else:
            temp[arr[left]] = left
            left += 1
        if (tarR in temp):
            return right, temp[tarR]
        else:
            temp[arr[right]] = right
            right -= 1
    return None
# 分割类双指针问题 partition

def partition_list(linkNode, target): ## 用到双指针了？
    LinkNode1 = Node()
    LinkNode2 = Node()
    left = LinkNode1
    right = LinkNode2
    start = linkNode
    while(start):
        if (start.dataval > target):
            left.nextval = start
            left = left.nextval
            start = start.nextval
        else:
            right.nextval = start
            right = right.nextval
            start = start.nextval
    right.nextval = None
    ansr = LinkNode2.nextval
    left.nextval = ansr
    return  LinkNode1.nextval

def reverse(str):#字符串翻转
    left = 0
    right = len(str) -1
    while left < right:
        str[left], str[right] = str[right] ,str[left]
        left += 1
        right -= 1
    return str

if __name__ == '__main__':
    ## 双指针
    ## 数据结构 数组 链表
    ## 类型
    #       同向双指针：无重复最长子串
                # 快慢双指针： 链表环的判断
    #       相向双指针：两数之和
    #       背向双指针：最长回文子串 k个最近的元素
    str ="baf7bbcd"
    arr = [6,1,2,3,4,5]
    k , x =4, 3
    head = creatLinkNode(7)
    # head = creatLinkNode_with_cycle(4,9)
    # print(find_cycle_entra(head))
    # printLinkNode(head)
    # print(longest_palindromic_substring(str))
    # print(find_k_closed_elements(arr, k, x))
    print(longest_substr_NoRep(str))
    # print(f_mid_point_link(head))
    # print(find_cycle_linkNode(head))
    # print('{0}'.format(find_two_sum(arr, 6)))
    # print(find_two_sum_v4(arr, 6))
    # printLinkNode(partition_list(head,3))
    print(reverse(arr))
    
    