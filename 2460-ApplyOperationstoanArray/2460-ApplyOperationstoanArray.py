class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        cnt = 0
        n = len(nums)

        for i in range(n):
            
            if i < n - 1 and nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                nums[i], nums[cnt] = 0, nums[i]
                cnt += 1
                  
        return nums