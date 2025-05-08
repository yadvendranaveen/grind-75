class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max_so_far = min_so_far = nums[0]

        for curr in nums[1:]: # focus on starting with 1
            temp_max = max(curr, curr*max_so_far, curr*min_so_far) 
            temp_min = min(curr, curr*max_so_far, curr*min_so_far)
            max_so_far, min_so_far = temp_max, temp_min
            ans = max(ans, max_so_far)
        return ans
