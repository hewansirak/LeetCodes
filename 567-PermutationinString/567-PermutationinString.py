class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False  # s1 can't be a substring if it's longer than s2

        # Create frequency arrays for 26 lowercase letters
        s1_count = [0] * 26
        window_count = [0] * 26

        # Function to get index of a character ('a' -> 0, 'b' -> 1, ..., 'z' -> 25)
        def char_index(ch):
            return ord(ch) - ord('a')

        # Populate the frequency array for s1 and the first window of s2
        for i in range(len(s1)):
            s1_count[char_index(s1[i])] += 1
            window_count[char_index(s2[i])] += 1

        # Check if first window is a match
        if s1_count == window_count:
            return True

        # Sliding window over s2
        for i in range(len(s1), len(s2)):
            new_char = s2[i]          # New character entering window
            old_char = s2[i - len(s1)]  # Character leaving window

            # Update window frequency
            window_count[char_index(new_char)] += 1
            window_count[char_index(old_char)] -= 1

            # Check if updated window matches s1 count
            if s1_count == window_count:
                return True

        return False
        