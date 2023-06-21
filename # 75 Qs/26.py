# [26. leetcode 133]


class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors


def F(node):
    oldToNew = {}
    
    def dfs(node):
        if node in oldToNew:
            return oldToNew[node]
        copy = Node(node.val)
        oldToNew[node] = copy
        for n in node.neighbors:
            copy.neighbors.append(dfs(n))
        return copy
    
    return dfs(node) if node else None
