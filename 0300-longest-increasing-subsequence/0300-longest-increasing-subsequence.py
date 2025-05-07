class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            idx = bisect_left(stack, num)
            if idx==len(stack):
                stack.append(num)
            else:   
                stack[idx] = num
        return len(stack)