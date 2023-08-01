class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        sortedC = sorted(c.items(), key=lambda pair: pair[1], reverse=True)

        ans, oddFlag = 0, False
        for _, cnt in sortedC:
            if cnt > 1:
                if cnt%2:
                    oddFlag = True
                    ans += cnt-1
                else:
                    ans += cnt
            else:
                oddFlag = True
                break
        return ans+oddFlag