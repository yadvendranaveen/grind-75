class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def numberOfWays(i, amount):
            if amount == 0: 
                return 1
            if i == len(coins):
                return 0
            if coins[i]>amount:
                return numberOfWays(i+1, amount)
            return numberOfWays(i, amount-coins[i])+numberOfWays(i+1, amount)
        
        return numberOfWays(0, amount)
                
        