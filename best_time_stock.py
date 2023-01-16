class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_price = float('inf')
        max_profits = 0
        for current_price in prices:
            if current_price < min_price:
                min_price = current_price
            elif(current_price - min_price) > max_profits:
                max_profits = current_price - min_price
            else:
                pass
        
        return max_profits
            