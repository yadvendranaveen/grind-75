class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack, removal_indices = [], []
        for i, letter in enumerate(s):
            if letter == '(':
                stack.append(i)
            if letter==')':
                if not stack:   removal_indices.append(i)
                else:   stack.pop()
        ans = ''
        for i in range(len(s)):
            if i not in stack+removal_indices:
                ans+=s[i]
        return ans


            
        