# Last updated: 6/21/2025, 11:15:11 PM
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        dialpad = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }

        result = ['']
        
        for digit in digits[::-1]:
            letters = dialpad[digit]
            length = len(letters)
            result = result * length  
            
            pivot = 0
            for letter in letters:
                for i in range(len(result) // length):
                    result[pivot] = letter + result[pivot]
                    pivot += 1
                    
        return result