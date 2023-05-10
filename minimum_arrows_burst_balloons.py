class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        # sort balons by x_start
        # points.sort()
        points.sort(key = lambda p: p[1])
        curr_end = points[0][1]
        count = 1
        for i, j in points[1:]:
            if i > curr_end:
                curr_end = j
                count += 1
        
        return count