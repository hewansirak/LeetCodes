# Last updated: 8/5/2025, 4:49:50 PM
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        window_size = 2 * k + 1
        n = len(nums)
        ans = [-1] * n

        if window_size > n:
            return ans
        
        s = 0
        pre = []
        
        for i in range(n):
            s += nums[i]
            pre.append(s)
        
        for i in range(k, n-k):
            s = pre[i+k] - pre[i-k] + nums[i-k]
            ans[i] = int(s / window_size)

        return ans
        