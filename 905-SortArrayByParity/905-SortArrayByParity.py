# Last updated: 12/10/2025, 8:57:38 PM
1class Solution:
2    def sortArrayByParity(self, nums: List[int]) -> List[int]:
3        evens = []
4        odds = []
5        
6        for num in nums:
7            if num % 2 == 0:
8                evens.append(num)  
9            else:
10                odds.append(num)   
11        
12        result = evens + odds
13        
14        return result 