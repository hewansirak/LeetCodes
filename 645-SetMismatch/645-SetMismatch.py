# Last updated: 12/5/2025, 9:54:17 PM
1class Solution:
2    def findErrorNums(self, nums: List[int]) -> List[int]:
3        s = set()
4        duplicate = -1
5
6        for n in nums:
7            if n in s:
8                duplicate = n
9            
10            s.add(n)
11
12        n = len(s) + 1
13        target = (n+1) * n//2
14
15        missing = target - sum(s)
16
17        return duplicate, missing