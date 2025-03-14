class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        n = len(nums)
        counter = 0
        for x in range(n):
            for y in range(n):
                if nums[x] + nums[y] < target and 0 <= x < y < n:
                    counter +=1
        return counter

        