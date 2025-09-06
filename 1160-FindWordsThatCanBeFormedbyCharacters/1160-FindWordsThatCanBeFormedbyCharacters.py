# Last updated: 9/6/2025, 9:06:38 PM
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0
        char_count = Counter(chars)
        for word in words:
            word_count = Counter(word)
            if all(word_count[char] <= char_count[char] for char in word):
                result += len(word)
        return result