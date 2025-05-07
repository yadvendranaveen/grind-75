from bisect import bisect_left

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Sort by width ASC, height DESC
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # Extract only heights
        heights = [h for _, h in envelopes]

        # LIS on heights
        stack = []
        for h in heights:
            idx = bisect_left(stack, h)
            if idx == len(stack):
                stack.append(h)
            else:
                stack[idx] = h
        return len(stack)