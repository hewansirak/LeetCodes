class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n - 1):
            min_index = i  
            for j in range(i + 1, n):
                if nums[j] > nums[min_index]:  
                    min_index = j
            nums[i], nums[min_index] = nums[min_index], nums[i]  
        
        distinct_count = 1
        third_max = nums[0]  

        for i in range(1, n):
            if nums[i] != nums[i - 1]: 
                distinct_count += 1
                if distinct_count == 3:
                    return nums[i]  
        
        return nums[0]
                