# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        # nonlocal res
        '''
        I got the hint about creating a global value from : https://leetcode.com/TKR_6/
        '''
        self.res = 0
        def sum_of_nodes(node):
            if not node: return 0
            left, right = sum_of_nodes(node.left), sum_of_nodes(node.right)
            self.res += abs(left - right)
            return node.val + left + right
        sum_of_nodes(root)
        return self.res