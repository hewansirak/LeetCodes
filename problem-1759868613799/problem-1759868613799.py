# Last updated: 10/7/2025, 11:23:33 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)
