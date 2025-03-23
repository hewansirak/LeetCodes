# Last updated: 3/23/2025, 9:39:13 PM
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        child = 0
        cookie = 0
        content_children = 0
        
        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                content_children += 1
                child += 1
            cookie += 1 
        
        return content_children