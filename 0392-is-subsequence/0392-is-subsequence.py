class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sn, tn = len(s), len(t)
        @cache
        def dfs(s_idx, t_idx):
            if s_idx==sn:    return True
            if t_idx==tn:    return False
            ans = dfs(s_idx, t_idx+1)
            if s[s_idx]==t[t_idx]:
                ans |= dfs(s_idx+1, t_idx+1)
            return ans
        return dfs(0,0)