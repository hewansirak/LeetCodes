# Last updated: 12/19/2025, 10:50:00 PM
1class Solution:
2    def minimumTime(self, s: str) -> int:
3        length, start, res = len(s), 0, len(s)
4        
5        for i, c in enumerate(s):
6            start = min(start + (c == "1") * 2, i + 1)
7            res = min(res, start + length - 1 - i)
8        
9        return res