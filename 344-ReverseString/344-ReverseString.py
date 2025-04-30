# Last updated: 4/30/2025, 10:25:24 PM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) -1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        