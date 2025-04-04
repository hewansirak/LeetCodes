# Last updated: 4/4/2025, 10:10:15 PM
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        DP_increase = [1 for i in range(n)]
        DP_decrease = [1 for i in range(n)] 
        for i in range(1, n):
            if i % 2 != 0:            
                if arr[i] > arr[i - 1]:
                    DP_increase[i] = max(1 + DP_increase[i - 1], 1)
                if arr[i] < arr[i - 1]:
                    DP_decrease[i] = max(1 + DP_decrease[i - 1], 1)
            else:
                if arr[i] > arr[i - 1]:
                    DP_decrease[i] = max(1 + DP_decrease[i - 1], 1)
                if arr[i] < arr[i - 1]:
                    DP_increase[i] = max(1 + DP_increase[i - 1], 1)
        return max(max(DP_increase), max(DP_decrease))