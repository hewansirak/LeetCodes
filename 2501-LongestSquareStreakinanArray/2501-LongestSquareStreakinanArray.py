# Last updated: 4/12/2025, 10:29:09 PM
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        num_set = set(nums)
        
        longest_streak = 0
        
        for num in nums:
            streak_length = 0
            current = num
            
            while current in num_set:
                streak_length += 1
                current = current * current  
            
            if streak_length >= 2:
                longest_streak = max(longest_streak, streak_length)
        
        return longest_streak if longest_streak >= 2 else -1        