# Last updated: 10/22/2025, 9:40:53 PM
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        diffs = []

        for costA, costB in costs:
            diffs.append([costB - costA, costA, costB])
        
        diffs.sort()
        result = 0
        
        for i in range(len(diffs)):
            if i < len(diffs) // 2:
                result += diffs[i][2]
            else:
                result += diffs[i][1]
        return result
               