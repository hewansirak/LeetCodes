# Last updated: 7/19/2025, 11:15:26 PM
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        iso = set(zip(s, t))
        return len(iso) == len(set(s)) == len(set(t))