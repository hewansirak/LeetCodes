class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:

        # cnt is the number of nonzero entries in the list (used to index our result)
        cnt = 0
        n = len(nums)

        for i in range(n):
            
            # Make sure we don't go out of bounds
            if i < n - 1 and nums[i] == nums[i + 1]:
                # Perform operations as described by the problem
                nums[i] *= 2
                nums[i + 1] = 0

            if nums[i] != 0:
                # Set nums[i] to 0, and nums[cnt] to the old value of nums[i]
                nums[i], nums[cnt] = 0, nums[i]
                cnt += 1
                  
        return nums