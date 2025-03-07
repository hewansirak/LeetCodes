class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        count = Counter(arr1)
        result = []

        for num in arr2:
            if num in count:
                result.extend([num] * count[num])  
                del count[num] 

        remaining = list(count.elements())  
        
        n = len(remaining)
        for i in range(n):
            min_index = i
            for j in range(i + 1, n):
                if remaining[j] < remaining[min_index]:
                    min_index = j
            remaining[i], remaining[min_index] = remaining[min_index], remaining[i] 

        result.extend(remaining)

        return result
        