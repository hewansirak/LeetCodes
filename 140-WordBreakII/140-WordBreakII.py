# Last updated: 10/29/2025, 11:45:25 PM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        memo = {}

        def backtrack(start):
            if start in memo:
                return memo[start]
            if start == len(s):
                return [""]

            results = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                
                if word in wordSet:
                    for sentense in backtrack(end):
                        if sentense:
                            results.append(word + " " + sentense)
                        else:
                            results.append(word)

            memo[start] = results
            return results

        return backtrack(0)