# Last updated: 9/15/2025, 9:11:39 PM
class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = Counter(nums)
        pairs = 0
        leftovers = 0
        
        for count in freq.values():
            pairs += count // 2
            leftovers += count % 2
        
        return [pairs, leftovers]