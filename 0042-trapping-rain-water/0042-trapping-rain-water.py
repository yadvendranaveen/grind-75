class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l2r, r2l = [0]*n, [0]*n
        
        u = height[0]
        for i, h in enumerate(height):
            if h > u:
                u = h
            else:
                l2r[i] = u - h
                
        u = height[-1]
        for i, h in reversed(list(enumerate(height))):
            if h > u:
                u = h
            else:
                r2l[i] = u - h
        
        return sum(map(min, zip(l2r, r2l)))
        
            
                
        