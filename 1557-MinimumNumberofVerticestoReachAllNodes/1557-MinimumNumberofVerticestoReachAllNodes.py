# Last updated: 6/22/2025, 10:48:15 PM
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        arr1, arr2 = [x[0] for x in edges], [x[1] for x in edges]
        arr1 = set(arr1)
        arr2 = set(arr2)
        for i in arr2:
            if i in arr1:
                arr1.remove(i)
        return([*arr1])