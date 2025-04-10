# Last updated: 4/10/2025, 9:10:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = Counter()
        left = 0
        longest = 0

        for right in range(len(s)):
            ct[s[right]] += 1 

            while ct[s[right]] > 1:
                ct[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest