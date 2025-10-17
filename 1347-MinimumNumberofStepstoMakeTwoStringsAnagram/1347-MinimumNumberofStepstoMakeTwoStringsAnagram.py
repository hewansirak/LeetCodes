# Last updated: 10/17/2025, 10:29:44 PM
class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        steps = 0
        
        for ch in count_s:
            if count_s[ch] > count_t[ch]:
                steps += count_s[ch] - count_t[ch]
                
        return steps