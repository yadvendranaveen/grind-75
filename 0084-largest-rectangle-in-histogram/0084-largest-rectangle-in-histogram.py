class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [-1] * n, [n] * n

        # Calculate left boundaries
        for i in range(1, n):
            prev = i - 1
            while prev >= 0 and heights[prev] >= heights[i]:
                prev = left[prev]
            left[i] = prev

        # Calculate right boundaries
        for i in range(n - 2, -1, -1):
            next = i + 1
            while next < n and heights[next] >= heights[i]:
                next = right[next]
            right[i] = next
        print(left, right, [heights[i] * (right[i] - left[i] - 1) for i in range(n)])

        # Calculate the maximum area
        return max(heights[i] * (right[i] - left[i] - 1) for i in range(n))
            