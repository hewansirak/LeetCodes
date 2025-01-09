class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        interval = set()
        l = 0

        for r in range(len(nums)):
            if r - l > k:
                interval.remove(nums[l])
                l += 1
            if nums[r] in interval:
                return True
            interval.add(nums[r])
        return False