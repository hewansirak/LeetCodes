# Last updated: 4/23/2025, 11:42:22 PM
class Solution:
    def removeStars(self, s: str) -> str:
        ans=[]
        for c in s:
            if c =='*':
                ans.pop()
            else:
                ans.append(c)
        return "".join(ans)
        