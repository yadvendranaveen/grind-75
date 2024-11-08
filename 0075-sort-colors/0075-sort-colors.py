class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, right, ptr = 0, len(nums)-1, 0
        
        while ptr<=right:
            if nums[ptr]==0:
                nums[left], nums[ptr] = nums[ptr], nums[left]
                left+=1
                ptr+=1
            elif nums[ptr]==2:
                nums[right], nums[ptr] = nums[ptr], nums[right]
                right-=1
            else:
                ptr+=1


        