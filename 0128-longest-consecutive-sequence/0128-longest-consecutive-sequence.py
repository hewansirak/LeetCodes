class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        max_length = 0

        if not nums:  
            return 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                streak = 1

                while current + 1 in num_set:
                    streak +=1
                    current += 1

                max_length = max(streak, max_length)

        return max_length
