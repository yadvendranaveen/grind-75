class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        
        letterMap = {'2': 'abc', '3':'def', '4':'ghi','5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        ans = []
        def backtrack(i, s):
            if i==len(digits):
                ans.append(s)
                return
            for letter in letterMap[digits[i]]:
                backtrack(i+1, s+letter)
        
        backtrack(0,'')
        return ans

        