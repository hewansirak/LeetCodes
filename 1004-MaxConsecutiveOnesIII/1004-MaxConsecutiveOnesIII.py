# Last updated: 4/10/2025, 10:03:25 PM
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        max_len = 0
        left = 0 
        n = len(nums)
        zeros = 0 

        for right in range(n):  
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_len = max(max_len, right - left + 1)
        return max_len
        