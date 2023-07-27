class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min, ans = float('inf'), 0
        for price in prices:
            if price<min:
                min = price
            elif price-min>ans:
                ans=price-min
        return ans