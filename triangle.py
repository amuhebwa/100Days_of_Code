class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or len(triangle) == 0:
            return 0
        
        triangle = triangle[::-1]
        dp = [0]*(len(triangle[0]) + 1)

        for sub_tria in triangle:
            for i, val in enumerate(sub_tria):
                dp[i] = val + min(dp[i], dp[i+1])
        # print(dp[0])
        return dp[0]