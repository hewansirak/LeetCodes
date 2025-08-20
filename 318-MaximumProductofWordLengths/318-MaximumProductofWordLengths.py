# Last updated: 8/20/2025, 11:45:26 PM
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = float('-inf')
        l, r = 0, 1
        while l < len(words) - 1:
            set1 = set(words[l])
            set2 = set(words[r])
            if not set1 & set2:
                res = max(res, len(words[l]) * len(words[r]))
            r += 1
            if r == len(words):
                l += 1
                r = l + 1
        return res if res != float('-inf') else 0