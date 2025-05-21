# Last updated: 5/21/2025, 9:41:37 PM
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = defaultdict(int)

        for c in s:
            count[c] += 1
        
        for i, c in enumerate(s):
            if count[c] == 1:
                return i
        return -1