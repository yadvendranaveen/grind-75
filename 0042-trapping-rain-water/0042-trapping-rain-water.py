class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l2r, r2l = [0]*n, [0]*n
        
        u = l = height[0]
        for i, h in enumerate(height):
            if h > u:
                u = h
            else:
                l = h
                l2r[i] = u - l
                
        u = l = height[-1]
        for i, h in reversed(list(enumerate(height))):
            if h > u:
                u = h
            else:
                l = h
                r2l[i] = u - l
        
        return sum(map(min, zip(l2r, r2l)))
        
            
                
        