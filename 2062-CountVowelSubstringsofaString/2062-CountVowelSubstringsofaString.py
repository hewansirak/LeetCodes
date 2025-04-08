# Last updated: 4/8/2025, 11:29:10 PM
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
        j, k, vow, res = 0, 0, 0, 0
        for i in range(len(word)):
            if word[i] in maps:
                maps[word[i]] += 1
                if maps[word[i]] == 1:
                    vow += 1
                while vow == 5:
                    maps[word[k]] -= 1
                    if maps[word[k]] == 0:
                        vow -= 1
                    k += 1
                res += k-j
            else:
                maps = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
                vow = 0
                j, k = i+1, i+1
        return res