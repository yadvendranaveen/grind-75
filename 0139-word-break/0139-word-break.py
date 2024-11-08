class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dfs(curr):
            if not curr: return True
            for word in wordDict:
                if curr.startswith(word) and dfs(curr[len(word):]):
                    return True
            return False
        return dfs(s)
        