# Last updated: 5/12/2025, 11:09:17 PM
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        max_num = max(nums)
        low, high = 1, max_num
        
        while low <= high:
            mid = (low + high) // 2
            total = 0
            for num in nums:
                total += (num + mid - 1) // mid  
                if total > threshold:
                    break
            if total <= threshold:
                high = mid - 1
            else:
                low = mid + 1
        
        return low