class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charIndex = {}
        max_length = 0
        left = 0
        
        for right in range(len(s)):
            current_char = s[right]
            
            if current_char in charIndex and charIndex[current_char] >= left:
                left = charIndex[current_char] + 1
            
            charIndex[current_char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length