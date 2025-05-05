class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        @cache
        def dfs(i):
            tail = nums[i]
            maxSubset = []
            for p in range(i):
                if tail % nums[p] == 0:
                    subset = dfs(p) 
                    if len(maxSubset) < len(subset):
                        maxSubset = subset
            maxSubset = maxSubset.copy()
            maxSubset.append(tail)
            return maxSubset
            
        ans = []
        nums.sort()
        for i in range(len(nums)):
            ans = max(dfs(i), ans, key = len)

        
        return ans