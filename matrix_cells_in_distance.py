class Solution:
    def calculate_distance(self, r, c, rCenter, cCenter):
        return abs(r-rCenter) + abs(c-cCenter)
    
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        
        result = {}
        for r in range(0, rows):
            for c in range(0, cols):
                distance = self.calculate_distance(r, c, rCenter, cCenter)
                # print((r, c), 'distance = ', distance)
                result.update({(r,c): distance})

        result = sorted(result.items(), key=lambda x:x[1])
        res = [v[0] for v in result]
        return res