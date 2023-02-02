# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return root
        
        _queue, results = [], []
        _queue.append(root)

        '''
        We will use BFS
        '''
        height = 0
        while _queue:
            temp_result = []
            for i in range(0, len(_queue)):
                temp_node =_queue.pop(0)
                if temp_node:
                    temp_result.append(temp_node.val)
                    if temp_node.left:
                        _queue.append(temp_node.left)
                    if temp_node.right:
                        _queue.append(temp_node.right)
            if height % 2 == 0:
                results.append(temp_result)
            else:
                results.append(temp_result[::-1])
            
            height += 1
        return results
            