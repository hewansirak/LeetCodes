# Last updated: 11/18/2025, 11:32:10 PM
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = Counter(arr)

        ans = -1
        for k, freq in count.items():
            if k == freq and k > ans:
                ans = k
        
        return ans