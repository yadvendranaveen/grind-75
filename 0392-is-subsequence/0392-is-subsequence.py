class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn, tn = len(s), len(t)
        # @cache
        def dfs(s_idx, t_idx):
            if s_idx==sn:    return True
            if t_idx==tn:    return False
            return dfs(s_idx+(s[s_idx]==t[t_idx]), t_idx+1)
        return dfs(0,0)