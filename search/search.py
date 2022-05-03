import collections
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
    
    def printTree(self):  # 中序遍历
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

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

def canMeasureWater( x: int, y: int, z: int) -> bool:
        stack = [(0, 0)]
        seen = set()
        while stack:
            remain_x, remain_y = stack.pop()
            if remain_x == z or remain_y == z or remain_x + remain_y == z:
                return True
            if (remain_x, remain_y) in seen:
                continue
            seen.add((remain_x, remain_y))
            # 把 X 壶灌满。
            stack.append((x, remain_y))
            # 把 Y 壶灌满。
            stack.append((remain_x, y))
            # 把 X 壶倒空。
            stack.append((0, remain_y))
            # 把 Y 壶倒空。
            stack.append((remain_x, 0))
            # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
            stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
            # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
            stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
        return False


def calcEquation(equations, values, queries):
    d = {}
    
    def dfs(d, start, end, route, covered):
        if end in d[start]:
            return route * d[start][end]
        else:
            for i in d[start]:
                if i not in covered:
                    a = dfs(d, i, end, route * d[start][i], covered + [i])
                    if a != -1:
                        return a
            return -1
    
    for i in range(len(equations)):
        a = equations[i][0]
        b = equations[i][1]
        if a not in d:
            d[a] = {b: values[i]} # 抽象思维与建图能力 https://leetcode-cn.com/problems/evaluate-division/solution/chu-fa-qiu-zhi-chou-xiang-si-wei-yu-jian-j8kf/
        else:
            d[a][b] = values[i] #https://leetcode-cn.com/problems/evaluate-division/solution/jian-dan-dfs-python24ms-by-qian-li-ma-8-qv1t/
        if b not in d:
            d[b] = {a: 1 / values[i]}
        else:
            d[b][a] = 1 / values[i]
    ans = []
    for i in queries:
        x = i[0]
        y = i[1]
        if x not in d or y not in d:
            ans.append(-1)
        elif x == y:
            ans.append(1)
        else:
            ans.append(dfs(d, x, y, 1, [x]))
    return ans

def pacificAtlantic(heights):
        m, n = len(heights), len(heights[0])

        def search(starts):
            visited = set() # 访问过的做标记
            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)): #坐标上下左右遍历
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        print(search(pacific))
        print(search(atlantic))
        for i in map(list, search(pacific) & search(atlantic)): #python map set函数用法  https://blog.csdn.net/qq_35608277/article/details/78661552
            print(i)
        return list(map(list, search(pacific) & search(atlantic))) # 取并集操作；把set转化为list集合


def serialize(root):
    """
    Encodes a tree to a single string.
    """
    
    def postorder(root):
        return postorder(root.left) + postorder(root.right) + [root.data] if root else []

    print(postorder(root))
    print(' '.join(map(str, postorder(root)))) # .join()的用法 https://www.runoob.com/python/att-string-join.html
    return ' '.join(map(str, postorder(root)))

def deserialize(data):
    """
    Decodes your encoded data to tree.
    """
    
    def helper(lower=float('-inf'), upper=float('inf')):
        if not data or data[-1] < lower or data[-1] > upper:
            return None
        
        val = data.pop()
        root = Node(val)
        root.right = helper(val, upper)
        root.left = helper(lower, val)
        return root
    
    data = [int(x) for x in data.split(' ') if x]
    return helper()
# 迷宫系列https://blog.csdn.net/bingque6535/article/details/113420474
def hasPath(self, maze, start, destination):# 迷宫 https://zhuanlan.zhihu.com/p/139475922
        visited = set()
        dirs = [0, 1, 0, -1, 0] #
        row, col = len(maze), len(maze[0])
    
        # DFS
        def dfs(i, j):
            if i == destination[0] and j == destination[1]:
                return True
            for k in range(4):
                move_i, move_j = i, j
                while 0 <= (t1 := move_i + dirs[k]) < row and 0 <= (t2 := move_j + dirs[k + 1]) < col and maze[t1][
                    t2] != 1:
                    move_i, move_j = t1, t2 # 满足条件则在这个方向上继续，不满足条件则跳出换向 （换向；一直走）
                if i == move_i and j == move_j: continue
                if (move_i, move_j) not in visited:
                    visited.add((move_i, move_j))
                    if dfs(move_i, move_j): return True
            return False
    
        # DFS
        def bfs(i, j):
            queue = collections.deque([[i, j]])
            visited.add((i, j))
            while queue:
                i, j = queue.pop()
                if [i, j] == destination: return True
                for k in range(4):
                    move_i, move_j = i, j# py3.8 := 海象运算符号https://www.cnblogs.com/wongbingming/p/12743802.html
                    while 0 <= (t1 := move_i + dirs[k]) < row and 0 <= (t2 := move_j + dirs[k + 1]) < col and maze[t1][t2] != 1:
                        move_i, move_j = t1, t2
                    if move_i == i and move_j == j: continue
                    if (move_i, move_j) not in visited:
                        visited.add((move_i, move_j))
                        queue.appendleft([move_i, move_j])
            return False
    
        return dfs(start[0], start[1])  # bfs(start[0], start[1])
if __name__ == '__main__':
    # 二分搜索查找：
    #    递归
    #    非递归
    
    arr = [1, 3, 5, 7, 9]
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"],["a", "a"], ["x", "x"]]
    # print(binary_search2(arr, 9))
    # print(canMeasureWater(3, 5,4))
    print(calcEquation(equations, values, queries))
    heights = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
    print(pacificAtlantic(heights))
    node = Node(None)
    node_array = [4, 3, 6, 5, 7, 8]
    node_array1 = [3, 9, 20, 15, 7]
    node_array_balen = [6, 5, 9]
    for item in node_array:
        node.insert(item)
    deserialize(serialize(node))
    
    
    
    
    
    
    
    
    
    
    