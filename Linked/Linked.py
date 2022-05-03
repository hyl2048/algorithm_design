class Node:
    def __init__(self,datavalue = None):
        self.datavalue = datavalue
        self.datanext = None
        
def createLinkedlist():
    head = Node(0)
    node = head
    for i in [9,9,9]:
        node.datanext = Node(i)
        node = node.datanext
    return head

def printLinkedlist(linkedlist):
    head = linkedlist
    while head:
        print(head.datavalue)
        if head.datanext == None:
            break
        head = head.datanext
        
    
    
    
def revers_linked_list_two(linkedlist, m, n):#翻转第m到n个
    pre = linkedlist
    for i in range(0,m-1):
        pre = pre.datanext
    cur = pre.datanext
    for i in range(m, n):# 写错了字母 调试好久 把 datanext 写成了datanaxt
        next = cur.datanext
        cur.datanext = next.datanext
        next.datanext = pre.datanext
        pre.datanext = next
        # next = cur.datanext
        # cur.datanext = next.datanext
        # next.datanext = pre.datanext
        # pre.datanext = next
    return linkedlist

def revLinklist(head, m , n):
    dummy_node = Node(-1)
    dummy_node.datanext = head
    pre = dummy_node
    for i in range( m - 1):
        pre = pre.datanext
    
    cur = pre.datanext
    for i in range(n - m):
        # nex = cur.datanext
        # cur.datanaxt = nex.datanext
        # nex.datanext = pre.datanext
        # pre.datanext = nex
        next = cur.datanext
        cur.datanext = next.datanext
        next.datanext = pre.datanext
        pre.datanext = next
    return head


def sortList(self, head: Node) -> Node:# https: // leetcode - cn.com / problems / sort - list / solution / pai - xu - lian - biao - by - leetcode - solution /
    def sortFunc(head: Node, tail: Node) -> Node:
        if not head:
            return head
        if head.next == tail:
            head.next = None
            return head
        slow = fast = head
        while fast != tail: # 不能让fast判空， 有时 fast.next.next 超出了分割的范围
            slow = slow.next
            fast = fast.next
            if fast != tail:
                fast = fast.next
        mid = slow
        return merge(sortFunc(head, mid), sortFunc(mid, tail))
    
    def merge(head1: Node, head2: Node) -> Node:
        dummyHead = Node(0)
        temp, temp1, temp2 = dummyHead, head1, head2
        while temp1 and temp2:
            if temp1.val <= temp2.val:
                temp.next = temp1
                temp1 = temp1.next
            else:
                temp.next = temp2
                temp2 = temp2.next
            temp = temp.next
        if temp1:
            temp.next = temp1
        elif temp2:
            temp.next = temp2
        return dummyHead.datanext
    
    return sortFunc(head, None)

def plusOne(head: Node) : # 给单链表加一 https://zhuanlan.zhihu.com/p/97229772

    def reverseList(head):
        if not head or not head.datanext:
            return head
        cur = reverseList(head.datanext)#  递归反转链表
        tmp = head.datanext
        tmp.datanext = head
        head.datanext = None
        return cur

    head = reverseList(head)
    p = head
    carry = 1
    while p:
        # carry 商， b余数
        carry, b = divmod(p.datavalue + carry, 10) # https://www.runoob.com/python/python-func-divmod.html
        p.datavalue = b
        if carry == 0: break
        if not p.datanext and carry: p.datanext = Node(0)
        p = p.datanext

    return reverseList(head)

# 将该二叉搜索树转换成一个排序的双向链表
# https://zhuanlan.zhihu.com/p/39025518

# 扁平化多级双向链表
# https://leetcode-cn.com/problems/flatten-a-multilevel-doubly-linked-list/


head = createLinkedlist()
# printLinkedlist(head)
# revLinkedlist = revers_linked_list_two(head,2,4)
# printLinkedlist(revLinkedlist)
plusOne(head)
# dummy node
#     dummy节点的创建
#     防止头结点被删掉
# 链表存在环
# 链表环的入口位置 有个公式 转n圈 再加上 若干步，这个若干步可以算出来  https://leetcode-cn.com/problems/linked-list-cycle-ii/

# 反转链表

# 重排链表

# 链表分割与拼接
#     https://leetcode-cn.com/problems/partition-list/solution/fen-ge-lian-biao-by-leetcode-solution-7ade/

# 排序链表 归并排序

# 双向链表

# 循环链表插入节点
# https://www.jianshu.com/p/e740c9b64a43