# Last updated: 12/14/2025, 11:07:23 PM
1class Solution:
2    def findMinDifference(self, timePoints: List[str]) -> int:
3
4        times = []
5        for time in timePoints:
6            hours, minutes = map(int, time.split(':'))
7            times.append(hours * 60 + minutes)
8        
9        times.sort()
10        
11        min_diff = float('inf')
12
13        for i in range(len(times) - 1):
14            min_diff = min(min_diff, times[i + 1] - times[i])
15        
16        min_diff = min(min_diff, 1440 + times[0] - times[-1])
17        
18        return min_diff