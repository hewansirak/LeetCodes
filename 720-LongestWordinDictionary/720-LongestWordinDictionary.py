# Last updated: 9/25/2025, 11:20:40 PM
class Solution:
    def longestWord(self, words: List[str]) -> str:
        word_set = set(words)
        best = ""

        for word in words:
            valid = True
            for i in range(1, len(word)):
                if word[:i] not in word_set:
                    valid = False
                    break

            if valid:
                if len(word) > len(best) or (len(word) == len(best) and word < best):
                    best = word

        return best
