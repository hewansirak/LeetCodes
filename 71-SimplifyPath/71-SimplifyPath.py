# Last updated: 5/25/2025, 9:41:29 PM
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        dirs = path.split('/')
        
        for dir in dirs:
            if dir == '' or dir == '.':
                continue
            
            if dir == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(dir)

        return '/' + '/'.join(stack)