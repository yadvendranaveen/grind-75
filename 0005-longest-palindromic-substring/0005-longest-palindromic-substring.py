class Solution:
    def longestPalindrome(self, s: str) -> str:

        def dfs(i,j):
            if i==j: return True
            if j==i+1: return s[i]==s[j]
            return s[i]==s[j] and dfs(i+1, j-1)

        for length in range(len(s), 0, -1):
            for start in range(len(s)-length+1):
                end = start+length-1
                if dfs(start, end): return s[start:end+1]
        