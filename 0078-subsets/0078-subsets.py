class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(i, arr):
            if i<0: 
                ans.append(arr[:])
                return 

            dfs(i-1, arr)

            arr.append(nums[i])
            dfs(i-1, arr)
            arr.pop()
        
        dfs(len(nums)-1, [])
        return ans
            
        
