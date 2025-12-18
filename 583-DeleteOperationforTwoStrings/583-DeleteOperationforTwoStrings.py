# Last updated: 12/18/2025, 11:09:43 PM
1class Solution:
2    def minDistance(self, word1: str, word2: str) -> int:
3        m = len(word1)
4        n = len(word2)
5        a = []
6        for i in range(m+1):
7            a.append([])
8            for j in range(n+1):
9                a[-1].append(0)
10        
11        for i in range(m):
12            for j in range(n):
13                if word1[i]==word2[j]:
14                    a[i+1][j+1] = 1 + a[i][j]
15                else:
16                    a[i+1][j+1] = max( a[i][j+1], a[i+1][j])
17					
18        return m + n - ( 2 * a [-1][-1] )