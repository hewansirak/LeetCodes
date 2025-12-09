# Last updated: 12/9/2025, 4:17:52 PM
1class Solution:
2    def largestMerge(self, word1: str, word2: str) -> str:
3        merge = []
4        i = j = 0
5        
6        while i < len(word1) and j < len(word2):
7
8            if word1[i:] > word2[j:]:
9                merge.append(word1[i])
10                i += 1
11            else:
12                merge.append(word2[j])
13                j += 1
14        
15        merge.extend(word1[i:])
16        merge.extend(word2[j:])
17        
18        return ''.join(merge)