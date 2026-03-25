class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buying_price = prices[0]
        best_profit = 0
        
        for selling_price in prices:
            buying_price = min(buying_price, selling_price)
            best_profit = max(best_profit, selling_price - buying_price)
        
        return best_profit