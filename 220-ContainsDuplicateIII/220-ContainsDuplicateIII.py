# Last updated: 12/13/2025, 11:25:59 PM
1class Solution:
2    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
3        if valueDiff < 0:
4            return False
5        
6        window = SortedList()
7        
8        for i, x in enumerate(nums):
9            left = window.bisect_left(x - valueDiff)
10            right = window.bisect_right(x + valueDiff)
11            
12            if left != right:
13                return True
14            window.add(x)
15            
16            if i >= indexDiff:
17                window.remove(nums[i - indexDiff])
18        
19        return False