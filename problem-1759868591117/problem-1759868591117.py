# Last updated: 10/7/2025, 11:23:11 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            if goal[i+1:] + goal[:i+1] == s:
                return True
        return False