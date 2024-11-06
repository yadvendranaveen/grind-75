class Solution:
    def findAnagrams(self, s: str, p: str):
        # Frequency map for characters in `p`
        p_count = Counter(p)
        s_count = Counter()
        
        # Lengths of the strings
        len_s, len_p = len(s), len(p)
        result = []
        
        for i in range(len_s):
            # Add current character to the window count
            s_count[s[i]] += 1
            
            # Remove the leftmost character if the window size exceeds len_p
            if i >= len_p:
                s_count[s[i - len_p]] -= 1
            
            # Check if the current window matches `p`'s frequency map
            if s_count == p_count:
                result.append(i - len_p + 1)
        
        return result
