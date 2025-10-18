# Last updated: 10/18/2025, 10:37:34 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        majority = []
        threshold = len(nums) // 3
        
        for element, count in count.items():
            if count > threshold:
                majority.append(element)
        
        return majority
