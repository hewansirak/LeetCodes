class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]  

    def reset(self) -> List[int]:
        return self.original[:]  

    def shuffle(self) -> List[int]:
        shuffled = self.original[:]  
        n = len(shuffled)
        for i in range(n):
            j = random.randint(i, n - 1) 
            shuffled[i], shuffled[j] = shuffled[j], shuffled[i]
        return shuffled    


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()