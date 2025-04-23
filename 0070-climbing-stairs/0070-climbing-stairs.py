class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def backtrack(curr):
            if curr<0:  return 0
            if curr==0: return 1
            return backtrack(curr-1)+backtrack(curr-2)

        return backtrack(n)
