"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        if not node:
            return None
        old_to_new = {}
        def dfs(node):
            if node in old_to_new:
                return old_to_new[node]
            new_node = Node(node.val) # create the node clone
            old_to_new[node] = new_node
            for neigh in node.neighbors:
                new_node.neighbors.append(dfs(neigh))
            return new_node
        return dfs(node)
        