# Last updated: 12/7/2025, 11:01:11 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        
4        for i in reversed(range(len(digits))):
5            
6            if digits[i] == 9:
7                digits[i] = 0
8            else:
9                digits[i] += 1
10                return digits
11        
12        return [1] + digits