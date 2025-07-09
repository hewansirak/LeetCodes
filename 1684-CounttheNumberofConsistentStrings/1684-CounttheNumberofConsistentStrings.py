# Last updated: 7/9/2025, 11:32:33 PM
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_set = set(allowed)
        char = 0
        for word in words:
            if all(char in allowed_set for char in word):
                char += 1
        return char