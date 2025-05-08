# Last updated: 5/8/2025, 11:09:18 PM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target >= letters[-1] or target < letters[0]:
            return letters[0]
        
        low = 0
        high = len(letters)-1
        while low <= high:
            mid = (high+low)//2
            
            if  target >= letters[mid]:
                low = mid+1
            
            if target < letters[mid]:
                high = mid-1
                
        return letters[low]