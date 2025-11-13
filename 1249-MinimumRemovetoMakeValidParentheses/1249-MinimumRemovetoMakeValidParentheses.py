# Last updated: 11/14/2025, 12:17:32 AM
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        remove = set()
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                if stack:
                    stack.pop()  # Match found
                else:
                    remove.add(i) 
        
        remove.update(stack)
        
        result = []
        for i, char in enumerate(s):
            if i not in remove:
                result.append(char)
        
        return ''.join(result)