class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ct = Counter()
        left = 0
        longest = 0

        for right in range(len(s)):
            # update the running variable
            ct[s[right]] += 1 # add the right element

            # validating
            while ct[s[right]] > 1: #abcabcbb
                ct[s[left]] -= 1
                left += 1

            # registering the answer
            longest = max(longest, right - left + 1)

        return longest