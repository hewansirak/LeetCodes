# Last updated: 4/8/2025, 11:44:48 PM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        abc = [-1, -1, -1]
        count, right = 0, 0
        while right < len(s):
            abc[ord(s[right]) - ord('a')] = right
            minIndex = min(abc)
            count += (minIndex + 1)
            right += 1
        return count