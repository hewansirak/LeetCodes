class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:

        ctr = Counter(nums)
        return nlargest(2, ctr, key = lambda x: ctr[x])