class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, m = [], {}
        for i in reversed(nums2):
            while stack and stack[-1]<=i:
                stack.pop()
            m[i] = stack[-1] if stack else -1
            stack.append(i)

        return list(map(lambda x: m[x], nums1))
        