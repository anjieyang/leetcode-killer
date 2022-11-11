"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        return self._clone(node, {})

    def _clone(self, node, copied):
        if node in copied:
            return copied[node]
        
        copy = Node(node.val)
        copied[node] = copy

        for neighbor in node.neighbors:
            copy.neighbors.append(self._clone(neighbor, copied))
        
        return copy