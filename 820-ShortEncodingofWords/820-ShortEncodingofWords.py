# Last updated: 10/12/2025, 11:34:10 PM
class TrieNode:
    def __init__(self, ch: Optional[str]='#'):
        self.ch = ch
        self.cd = {}  # children nodes
        self.end = False
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            if word[~i] not in curr.cd:
                curr.cd[word[~i]] = TrieNode(word[~i])
            curr = curr.cd[word[~i]]
        curr.end = True  

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = Trie()
        for word in words:
            trie.add(word)
        def dfs(node: TrieNode, curr: int) -> int:
            return sum(dfs(adj, curr+1) for adj in node.cd.values()) if node.cd else curr
        return dfs(trie.root, 1)