import collections
def BFS(self, node):
    queue = collections.deque([node])
    distance = {node : 0}
    
    while queue:
        node = queue.popleft()
        for neighbor in node.get_neighbors():
            if neighbor in distance:
                continue
            distance[neighbor] = distance[node] + 1
            queue.append(neighbor)
    