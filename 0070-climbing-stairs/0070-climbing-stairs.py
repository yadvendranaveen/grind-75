class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def backtrack(curr):
            if curr<0:  return 0
            if curr==0: return 1
            if curr in memo:    return memo[curr]
            memo[curr] = backtrack(curr-1)+backtrack(curr-2)
            return memo[curr]

        return backtrack(n)
