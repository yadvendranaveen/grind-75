class Solution:
    def findAnagrams(self, s: str, p: str):
        p_count = Counter(p)
        s_count = Counter()
        
        len_s, len_p = len(s), len(p)
        result = []
        
        for i in range(len_s):
            s_count[s[i]] += 1
            
            if i >= len_p:
                s_count[s[i - len_p]] -= 1
            
            if s_count == p_count:
                result.append(i - len_p + 1)
        
        return result
