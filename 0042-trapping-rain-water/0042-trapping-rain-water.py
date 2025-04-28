class Solution:
    def trap(self, height: List[int]) -> int:
        l2r = height[:]
        for i in range(1, len(height)):
            l2r[i] = max(l2r[i-1], l2r[i])
        r2l = height[:]
        for i in range(len(height)-2, -1, -1):
            r2l[i] = max(r2l[i+1], r2l[i])

        max_possible_water_heights = list(map(min, zip(l2r, r2l)))
        ans = 0
        for i in range(len(height)):
            ans += max_possible_water_heights[i]-height[i]
        return ans