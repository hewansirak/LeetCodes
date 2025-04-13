# Last updated: 4/13/2025, 10:29:07 PM
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, right = 0, 0
        count_nums = {}
        ans = 0
        cur_pairs = 0
        while right < len(nums):
            if nums[right] in count_nums:
                old_pairs = (count_nums[nums[right]] * (count_nums[nums[right]]-1))//2
                count_nums[nums[right]] +=1
                new_pairs = (count_nums[nums[right]] * (count_nums[nums[right]]-1))//2
                cur_pairs -= old_pairs
                cur_pairs += new_pairs
            else:
                count_nums[nums[right]] = 1
            
            while cur_pairs >= k and left < right:
                ans += (len(nums)-right)
                if count_nums[nums[left]] == 1:
                    count_nums.pop(nums[left])
                else:
                    old_pairs = (count_nums[nums[left]] * (count_nums[nums[left]]-1))//2
                    count_nums[nums[left]] -= 1
                    new_pairs = (count_nums[nums[left]] * (count_nums[nums[left]]-1))//2
                    cur_pairs -= old_pairs
                    cur_pairs += new_pairs
                left+=1
            right+=1
        
        return ans