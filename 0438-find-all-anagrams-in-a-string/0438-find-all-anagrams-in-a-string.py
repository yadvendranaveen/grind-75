class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ns, np = len(s), len(p)

        ans = []
        for i in range(ns):
            word = s[i:i+np]
            if Counter(word)==Counter(p):
                ans.append(i)
        return ans
        