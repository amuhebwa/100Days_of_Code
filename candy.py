class Solution:
    def candy(self, ratings: List[int]) -> int:
        '''
        [1, 0, 2]
        2, 1, 2 = 5

        [1, 2 ,2 ]
        1, 2, 1 = 4

        [1, 2, 3, 4, 5]
        1, 2, 3, 4, 5

        [1, 2, 3, 4, 5,  4, 3, 1]
         1, 2, 3, 4, 5[4], 3, 2, 1

         x, y, z
        '''
        n = len(ratings)
        candies = [1]*n
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = max(candies[i], candies[i-1] + 1)
                # candies[i] = candies[i-1] + 1
                # candies[i] += candies[i-1]
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1]+1)
        return sum(candies)








    



