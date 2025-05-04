class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        ans = 0
        while not all(nums[i]<=nums[i+1] for i in range(len(nums)-1)):
            min_sum = math.inf
            min_pair_idx = -1
            for i in range(len(nums)-1):
                pair_sum = nums[i] + nums[i+1]
                if pair_sum < min_sum:
                    min_sum = pair_sum
                    min_pair_idx = i
            new_num = nums[min_pair_idx] + nums[min_pair_idx+1]
            nums = nums[:min_pair_idx]+[new_num]+nums[min_pair_idx+2:]
            ans +=1
        return ans

