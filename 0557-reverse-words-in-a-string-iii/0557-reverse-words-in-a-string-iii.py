class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(list(map(lambda x: ''.join(list(reversed(x))), s.split())))
        