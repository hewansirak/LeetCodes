class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

        n = len(nums)

        for i in range(1, n):
            key = nums[i]
            j = i - 1

            while j >= 0 and nums[j] > key:  
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = key 

        result = []
        for i in range(n):
            if nums[i] == target:
                result.append(i)

        return result
            