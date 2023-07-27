class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'{':'}', "(":")", '[':']'}
        for i in s:
            if i in '{[(':
                stack.append(i)
            elif len(stack)==0 or i!=pairs[stack.pop()]:
                    return False
        return len(stack)==0
