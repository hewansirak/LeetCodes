# Last updated: 8/7/2025, 10:07:07 PM
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) == 1:
            return list(words[0]) 
        res = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res