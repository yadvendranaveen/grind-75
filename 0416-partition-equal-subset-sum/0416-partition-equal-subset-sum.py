class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total%2==1:  return False 

        @cache
        def dfs(idx, rem):
            if rem==0:  return True
            if idx<0:   return False
            return dfs(idx-1, rem) or dfs(idx-1, rem-nums[idx])

        return dfs(len(nums)-1, total//2)
        