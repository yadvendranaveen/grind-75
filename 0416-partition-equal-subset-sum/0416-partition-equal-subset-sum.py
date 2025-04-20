class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target%2==1:
            return False
        target //= 2

        n = len(nums)

        memo = {}
        def backtrack(idx, total):
            if total==target:   return True
            if total>target or idx==n:  return False
            if (idx,total) in memo:    return memo[(idx,total)]
            memo[(idx,total)] = backtrack(idx+1, total+nums[idx]) or backtrack(idx+1, total)
            return memo[(idx,total)]

        return backtrack(0,0)