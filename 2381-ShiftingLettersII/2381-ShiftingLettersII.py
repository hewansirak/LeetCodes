# Last updated: 4/7/2025, 9:05:30 PM
class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff_array = [0] * n  

        for start, end, direction in shifts:
            if direction == 1:  
                diff_array[start] += 1  
                if end + 1 < n:
                    diff_array[end + 1] -= 1  
            else: 
                diff_array[start] -= 1  
                if end + 1 < n:
                    diff_array[end + 1] += 1

        cumulative_shift = 0
        result = list(s)  

        for i in range(n):
            cumulative_shift = (cumulative_shift + diff_array[i]) % 26  
            if cumulative_shift < 0:
                cumulative_shift += 26 

            new_char = chr((ord(s[i]) - ord('a') + cumulative_shift) % 26 + ord('a'))
            result[i] = new_char  

        return "".join(result)