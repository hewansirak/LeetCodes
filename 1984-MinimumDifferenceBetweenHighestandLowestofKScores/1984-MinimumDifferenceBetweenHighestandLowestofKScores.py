class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        min_variation = float('inf')
        
        for i in range(len(nums) - k + 1):
            current_variation = nums[i + k - 1] - nums[i]
            
            if current_variation < min_variation:
                min_variation = current_variation
        
        return min_variation
            