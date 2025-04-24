class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l2r_min = list(accumulate(prices, min))
        r2l_max = list(accumulate(reversed(prices), max))[::-1]
        ans = 0
        for l,h in zip(l2r_min, r2l_max):
            ans = max(ans, h-l)
        return ans
            
            


        