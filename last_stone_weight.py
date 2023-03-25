class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        
        while len(stones) > 1:
            stones.sort()
            #heaviest = stones.pop()
            #second_heaviest = stones.pop()
            after_smashing = abs(stones.pop() - stones.pop())
            stones.append(after_smashing)
        
        return stones[0]