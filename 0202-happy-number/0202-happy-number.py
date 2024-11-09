class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n!=1:
            if n in hashset:    return False
            hashset.add(n)
            n=str(n)
            n = sum(map(lambda x: int(x)**2, n))
        return True