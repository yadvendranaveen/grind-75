class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rc = Counter(ransomNote)
        rm = Counter(magazine)
        
        for alphabet, count in rc.items():
            if count > rm[alphabet]:
                return False
        return True