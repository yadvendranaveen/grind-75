class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            if not stack or stack[-1]<num:
                stack.append(num)
                continue
            idx = bisect_left(stack, num)
            stack[idx] = num
            
        return len(stack)