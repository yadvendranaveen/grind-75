class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sc, tc = Counter(s), Counter(t)
        return sc==tc