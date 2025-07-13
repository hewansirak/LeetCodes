# Last updated: 7/13/2025, 11:02:29 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
    
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        freq_list = [(num, count) for num, count in freq.items()]
        freq_list.sort(key=lambda x: x[1], reverse=True)  

        result = []

        for i in range(k):
            result.append(freq_list[i][0])  

        return result   