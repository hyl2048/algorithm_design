class Node:
    def __init__(self,datavalue = None):
        self.datavalue = datavalue
        self.datanext = None
        
def createLinkedlist(size):
    head = Node(0)
    node = head
    for i in range(1,size):
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

head = createLinkedlist(6)
printLinkedlist(head)
revLinkedlist = revers_linked_list_two(head,2,4)
printLinkedlist(revLinkedlist)


        
    