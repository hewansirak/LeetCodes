# Last updated: 10/4/2025, 11:31:23 PM
class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = defaultdict(list)
        for word in words:
            trie[word[0]] += [word]
        
        res = 0
        for c in s:
            temp = list(trie[c])
            trie[c] = []
            while temp:
                word = temp.pop()
                if len(word) == 1:
                    res += 1
                else:
                    trie[word[1]] += [word[1:]]
        return res