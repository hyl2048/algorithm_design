import collections
import copy

from conda.auxlib import collection


class Node:
    
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data
            
    def printTree(self):# 中序遍历
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()
class AVL(object):
    def __init__(self):
        self.root = None
    
    def left_high(self, node):
        if node is None:
            return 0
        return self.tree_height(node.left)
    
    def right_high(self, node): # 左树高
        if node is None:
            return 0
        return self.tree_height(node.right)
    
    def tree_height(self, node): # 树高
        if node is None:
            return 0
        return max(self.tree_height(node.left), self.tree_height(node.right)) + 1
    
    def left_rotate(self, node): # 左旋转  https://blog.csdn.net/weixin_45666566/article/details/108092977
        if node is None:
            return
        new_node = copy.deepcopy(node)
        new_node.left = node.left
        new_node.right = node.right.left
        node.data = node.right.data
        node.right = node.right.right
        node.left = new_node
    
    def right_rotate(self, node): #右旋转
        if node is None:
            return
        new_node = copy.deepcopy(node)
        new_node.right = node.right
        new_node.left = node.left.right
        node.data = node.left.data
        node.left = node.left.left
        node.right = new_node
    
    def insert(self, data):# 非递归加添节点
        node = Node(data)
        if self.root is None:
            self.root = node
            return
        queue = [self.root]
        while queue:
            temp_node = queue.pop(0)
            if node.data < temp_node.data:
                if temp_node.left is None:
                    temp_node.left = node
                    return
                else:
                    queue.append(temp_node.left)
            if node.data >= temp_node.data:
                if temp_node.right is None:
                    temp_node.right = node
                    return
                else:
                    queue.append(temp_node.right)
    # def insert(self, root, data): #递归实现AVL
    #     node = Node(data)
    #     if root is None:
    #         self.root = node
    #         return
    #     if data < root.data:
    #         if not root.left:
    #             root.left = node
    #             return
    #         else:
    #             self.insert(root.left, data)
    #     else:
    #         if not root.right:
    #             root.right = node
    #             return
    #         else:
    #             self.insert(root.right, data)
    
    def make_balence1(self, node):# 简单的 LL, RR, LR , RL ，并非对存在不平衡的二叉树进行调整
        if self.right_high(node) - self.left_high(node) > 1:
            if node.right and self.left_high(node.right) > self.right_high(node.right):
                self.right_rotate(node.right)
                self.left_rotate(node.root)
            else:
                self.left_rotate(self.root)
        if self.left_high(node) - self.right_high(node) > 1:
            if node.left and self.right_high(node.left) > self.left_high(node.left):
                self.left_rotate(node.left)
                self.right_rotate(node.root)
            else:
                self.right_rotate(self.root)
        
        
    def judge_balence(self, root):# 分治法
        isbalence, _ = self.judge_balence_children(root)
        return isbalence
        
    def judge_balence_children(self, root):
        if root is None:
            return True, 0
        isbalenceL, heighL = self.judge_balence_children(root.left)
        isbalenceR, heighR = self.judge_balence_children(root.right)
        heigh = max(heighL, heighR) + 1
        if not isbalenceL or not isbalenceR:
            return False, heigh
        if abs(heighL - heighR) > 1:
            return False, heigh
        return True, heigh
        
    def in_order(self, node): # 中序遍历递归实现
        if node is None:
            return
        self.in_order(node.left)
        print(node.data)
        self.in_order(node.right)
    
    def in_order_no(self, node):# 中序遍历非递归实现
        stack = []
        temp = node
        if not temp:
            return []
        while temp or stack:
            while temp:
                stack.append(temp)
                temp = temp.left
            if stack:
                atemp = stack.pop()
                temp = atemp.right
                print(atemp.data)
                
                
    def pre_order(self, node):
        if node is None:
            return
        print(node.data)
        self.pre_output(node.left)
        self.pre_output(node.right)
    
    def pre_order_no(self, node):
        if node is None:
            return []
        temp = node
        stack = []
        while temp or stack:
            while temp:
                stack.append(temp)
                print(temp.data)
                temp = temp.left
            if stack:
                atemp = stack.pop()
                temp = atemp.right
            
    
    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)
        
    def post_order_no(self, node): #https://leetcode-cn.com/problems/binary-tree-postorder-traversal/solution/die-dai-jie-fa-shi-jian-fu-za-du-onkong-jian-fu-za/
        if node is None:
            return []
        stack = []
        res = []
        temp = node
        while temp or stack:
            while temp:
                res.append(temp.data)
                stack.append(temp)
                temp = temp.right
            if stack:
                atemp = stack.pop()
                temp = atemp.left
        return res[::-1] # 输出逆序  前序遍历和后序遍历的倒置关系， 前序遍历代码修改后得 后续遍历代码
    
    def BFS(self, node): # 层次遍历 队列
        if node is None:
            return []
        queque = []
        queque.append(node)
        while queque:
            atemp = queque.pop(0)
            print(atemp.data)
            if atemp.left:
                queque.append(atemp.left)
            if atemp.right:
                queque.append(atemp.right)
    
    def leverl_order_travel(self, root):
        if root is  None:
            return []
        queue = []
        queue = collections.deque([root, None])
        res = []
        level =[]
        queue.append(root)
        queue.append(None)
        while queue is not None:
            temp = queue.pop(0)
            if temp is None:
                res.append(level)
                queue.append(None)
                level = []
                if queue[0] is None:
                    return res
            else:
                level.append(temp.data)
                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
        return res
        

class BSTIterator: # 二叉树中序遍历 非递归写法v1
    def __init__(self, root):
        self.stack = []
        self.find_most_left(root)
    
    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def hasnext(self):
        return len(self.stack)
    
    def next(self):
        node = self.stack[-1]
        if node.right is not None:
            n = node.right
            while n != None:
                self.stack.append(n)
                n = n.left
        else:
            n = self.stack.pop()
            while self.stack and self.stack[-1].right == n:
                n = self.stack.pop()
        return node
        
        
    
class BSTIterator2: #二叉树中序遍历 非递归写法v2 优化版 代码风格 模块化 栈中所存数据为未遍历过右节点的节点
    def __init__(self, root):
        self.stack = []
        self.find_most_left(root)

    def find_most_left(self, node):
        while node:
            self.stack.append(node)
            node = node.left
    
    def hasnext(self):
        return bool(self.stack)
    
    def next(self):
        node = self.stack.pop()
        if node.right:
            self.find_most_left(node.right)
        return node
        
if __name__ == "__main__":
    ## 分治法可解决二叉树99%的问题
    
    
    # 二叉树：
    #    创建：
    #
    #    遍历：
    #       先序遍历：
    #          递归写法
    #          非递归写法
    #       中序遍历：
    #          递归写法
    #          非递归写法
    #       后序遍历：
    #          递归写法
    #          非递归写法
    #       层次遍历
    #    平衡二叉树：
    #       平衡判断
    #       平衡调整：
    #           LL
    #           LR
    #           RR
    #     搜索：
    #       BST(二分查找树)
    #       BFS：
    #
    #          模板
    #          应用场景
    #       DFS
    #       BFS+DFS
    
    #     红黑树(balence BST)：
    
    tree = AVL()
    node_array = [4, 3, 6, 5, 7, 8]
    node_array_balen = [6, 5, 9]
    for item in node_array:
        tree.insert(item)
    # print(tree.mid_output(tree.root))
    # tree.mid_output_no(tree.root)
    # tree.pre_output_no(tree.root)
    # res = tree.back_output_no(tree.root)
    # print(res[::-1])
    # tree.BFS(tree.root)
    print(tree.leverl_order_travel(tree.root))
        