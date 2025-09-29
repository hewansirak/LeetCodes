# Last updated: 9/29/2025, 11:40:18 PM
class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        self.suggestions = list()

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        root = TrieNode()
        products.sort()
        
        for product in products:
            cur = root
            for letter in product:
                if letter not in cur.children:
                    cur.children[letter] = TrieNode()
                cur = cur.children[letter]
        
                if len(cur.suggestions) < 3:
                    cur.suggestions.append(product)
            
            cur.end = True
            
        res = [[]] * len(searchWord)
        
        cur = root
        
        for i in range(len(searchWord)):
            if searchWord[i] not in cur.children:
                break
            
            cur = cur.children[searchWord[i]]
            res[i] = cur.suggestions
        
        return res