class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        for i in range(1, len(prices)):
            profit.append(prices[i]-prices[i-1])
        
        return sum(filter(lambda x:x>0, profit))