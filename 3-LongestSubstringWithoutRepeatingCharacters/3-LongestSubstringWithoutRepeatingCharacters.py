# Last updated: 10/25/2025, 9:43:21 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = Counter()
        left = 0
        longest = 0

        for right in range(len(s)):
            count[s[right]] += 1 

            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest