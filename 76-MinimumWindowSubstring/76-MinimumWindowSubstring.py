# Last updated: 4/11/2025, 11:07:33 PM
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t:
            return ""

        t_freq = defaultdict(int)
        for char in t:
            t_freq[char] += 1

        left = 0
        min_length = float('inf')
        min_window = ""
        required = len(t_freq)  
        formed = 0 
        window_freq = defaultdict(int)

        for right in range(len(s)):
            char = s[right]
            window_freq[char] += 1

            if char in t_freq and window_freq[char] == t_freq[char]:
                formed += 1

            while formed == required:
                current_window_length = right - left + 1
                if current_window_length < min_length:
                    min_length = current_window_length
                    min_window = s[left:right + 1]

                left_char = s[left]
                window_freq[left_char] -= 1

                if left_char in t_freq and window_freq[left_char] < t_freq[left_char]:
                    formed -= 1

                left += 1

        return min_window if min_length != float('inf') else ""
            