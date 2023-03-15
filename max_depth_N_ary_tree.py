"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        # base case
        if root is None:
            return 0
        
        depth = 1
        for child in root.children:
            depth = max(self.maxDepth(child) + 1, depth)
        return depth