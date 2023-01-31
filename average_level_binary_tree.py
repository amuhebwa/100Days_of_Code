# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        '''
        -Use Breadth First Search implement with a queue 
        -queue -> First in, First out i.e., push element into queue (append()), get it out first(pop(0))
        Note: pop() != pop(0)
        '''
        _queue, result = [], []
        _queue.append(root)
        while _queue:
            n = len(_queue)
            _sum = 0
            for i in range(0, n):
                temp_node = _queue.pop(0) # remove the node added first
                _sum += temp_node.val
                if temp_node.left:
                    _queue.append(temp_node.left) # now add the left node 
                if temp_node.right:
                    _queue.append(temp_node.right) # then append the right node 
            result.append(_sum/n)
        
        return result