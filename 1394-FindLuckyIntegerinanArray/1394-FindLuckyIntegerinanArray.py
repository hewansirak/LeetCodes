# Last updated: 11/17/2025, 11:43:28 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        luckiest = -1
        
        for num in range(1, 501):
            count = 0
            
            for i in range(len(arr)):
                if arr[i] == num:
                    count += 1
            
            if count == num:
                luckiest = max(luckiest, num)
        
        return luckiest