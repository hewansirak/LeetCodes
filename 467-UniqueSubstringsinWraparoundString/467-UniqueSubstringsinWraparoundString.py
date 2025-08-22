# Last updated: 8/22/2025, 11:52:09 PM
class Solution:
    def findSubstringInWraproundString(self, s: str) -> int:
        n = len(s)
        dp = [0] * 26
        curr_leng = 1        
        dp[ord(s[0]) - 97] = 1
        
        for i in range(1, n):
            # zab
            if (ord(s[i]) - ord(s[i - 1])) % 26 == 1 :
                curr_leng += 1
            else:
                curr_leng = 1
                
            idx = ord(s[i]) - 97
            dp[idx] = max(dp[idx], curr_leng)
                
        return sum(dp)
            