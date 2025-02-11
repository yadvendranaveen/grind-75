class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        running_min = math.inf
        max_profit = 0

        for price in prices:
            running_min = min(running_min, price)
            max_profit = max(max_profit, price-running_min)
        return max_profit
            
            


        