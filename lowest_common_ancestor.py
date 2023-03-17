# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_depth(self, root):
        if not root or root is None:
            return 0
        return 1 + max(self.find_depth(root.left), self.find_depth(root.right))
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root or root is None:
            return root
        '''
        Step 1: find the depth of the binary tree
        
        '''
        left_height = self.find_depth(root.left)
        right_height = self.find_depth(root.right)
        if left_height == right_height:
            return root
        elif left_height > right_height:
            return self.lcaDeepestLeaves(root.left)
        else:
            return self.lcaDeepestLeaves(root.right)
        