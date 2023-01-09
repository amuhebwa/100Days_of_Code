import math
from typing import List
class Solution:
    def calc_sqrt(self, current_point):
        result = math.sqrt((current_point[0] - 0)**2 + (current_point[1] - 0)**2)
        return round(result, 3)

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        if len(points) < 2:
            return points

        square_roots = {}
        for index, point in enumerate(points):
            square_root = self.calc_sqrt(point)
            square_roots.update({square_root: point})
        sorted_keys = sorted(square_roots)[:k]
        result = []
        for key in sorted_keys:
            result.append(square_roots.get(key))
        return result
        """
        points.sort(key = lambda P: P[0]**2 + P[1]**2)
        return points[:k]
