# Last updated: 8/11/2025, 10:36:04 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split()[::-1])

        