class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        sum_gains = []
        _current_gain = 0
        sum_gains.append(_current_gain)
        for i in range(0, len(gain)):
            _current_gain += gain[i]
            sum_gains.append(_current_gain)
        
        return max(sum_gains)