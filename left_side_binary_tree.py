# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        queue, result = [], []
        queue.append(root)
        while queue:
            x = []
            for i in range(len(queue)):
                temp = queue.pop(0)
                if temp:
                    x.append(temp.val)
                    if temp.left:
                        queue.append(temp.left)
                    if temp.right:
                        queue.append(temp.right)
            result.append(x.pop())
            print('-'*10)
        return result