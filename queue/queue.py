# 数组实现队列
class Array(object):
    def __init__(self,size = 32):
        self._size = size
        self._items = [None] * 32
    
    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return self._size
    
    def clean(self,value = None ):
        for i in range(len(self._items)):
            self._items[i] = None
    
    def __iter__(self):
        for item in self._items:
            yield item

class ArrayQueue(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.array = Array(maxsize)
        self.head = 0
        self.tail = 0
    
    def push(self, value):
        if len(self) >= self.maxsize:
            raise Exception('queue full')
        self.array[self.head % self.maxsize] =value
        self.head += 1
        
    def pop(self):
        value = self.array[self.tail % self.maxsize]
        self.tail += 1
        return value
    
    def __len__(self):
        return self.head - self.tail
    

def test_arrayqueue():
    import  pytest
    size = 5
    q = ArrayQueue(size)
    for i in range(size):
        q.push(i)
    for i in range(size+1):
        q.pop()
    print(q.tail )
    print(q.head)
    # assert len(q) == 0

# test_arrayqueue()
# 链表实现队列

class Node:
    def __init__(self,datavalue):
        self.datavalue = datavalue
        self.datanext = None

class head:
    def __init__(self):
        self.left = None
        self.right = None




class Linkedqueue:
    def __init__(self):
        self.head = head()
    
    def push(self,value):
        newNode = Node(value)
        p = self.head
        if p.right:
            temp = p.right
            p.right = newNode
            temp.datanext = newNode
        else:
            p.right = newNode
            p.left = newNode
        
    def pop(self):
        p = self.head
        if p.left and p.left == p.right:
            temp = p.left
            p.left = p.right = None
            return temp.datavalue
        elif p.left and p.left != p.right:
            temp = p.left
            p.left = temp.datanext
            return temp.datavalue
        else:
            raise LookupError('empty')
    
    def is_empty(self):
        if self.head.left:
            return False
        else:
            return True
    
    def top(self):
        if self.head.left:
            return self.head.left.value
        else:
            raise LookupError('empty')

def test_LinkQueue():
    queue = Linkedqueue()
    queue.push(3)
    print(queue.pop())

# test_LinkQueue()

