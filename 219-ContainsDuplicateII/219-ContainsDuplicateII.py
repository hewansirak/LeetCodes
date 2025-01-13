class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hset = {}

        for index in range(len(nums)):
            if nums[index] in hset and abs(index - hset[nums[index]]) <= k:
                return True
            hset[nums[index]] = index
        return False