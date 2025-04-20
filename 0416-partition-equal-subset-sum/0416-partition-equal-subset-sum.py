class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        target = sum(nums)
        if target%2==1:
            return False
        target //= 2

        n = len(nums)

        @cache
        def backtrack(idx, total):
            if total==target:   return True
            if idx==n:  return False

            return backtrack(idx+1, total+nums[idx]) or backtrack(idx+1, total)

        return backtrack(0,0)