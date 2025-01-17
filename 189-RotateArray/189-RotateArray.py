class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        tmp = [0] * n
        for i in range(n):
            tmp[(i + k) % n] = nums[i]
        
        nums[:] = tmp