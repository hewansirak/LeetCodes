# Last updated: 12/16/2025, 12:00:42 AM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        n, m = len(s), len(p)
4        
5        dp = [False] * (m + 1)
6        
7        dp[0] = True
8        
9        for j in range(1, m + 1):
10            if p[j - 1] == '*':
11                dp[j] = dp[j - 1]
12            else:
13                break  
14        
15        for i in range(1, n + 1):
16            new_dp = [False] * (m + 1)
17            for j in range(1, m + 1):
18                if p[j - 1] == '*':
19                    new_dp[j] = new_dp[j - 1] or dp[j]
20                elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
21                    new_dp[j] = dp[j - 1]
22                else:
23                    new_dp[j] = False
24            dp = new_dp
25            dp[0] = False
26        
27        return dp[m]