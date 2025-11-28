# Last updated: 11/28/2025, 10:00:18 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        
4        reverse = 0
5        sign = -1 if x < 0 else 1
6        x = abs(x)
7
8        while x != 0:
9
10            if  reverse > (2**31 - 1) //10 :
11                return 0
12        
13            last = x % 10
14            reverse = (reverse * 10 ) + last
15            x = x // 10
16            
17        return sign * reverse
18            