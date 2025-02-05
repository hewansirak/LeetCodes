class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def backtrack(address, s, ans, chunk):
            if chunk == 4:
                if not s: 
                    ans.append(address[:-1])  
                return
            
            for i in range(1, 4):
                if i > len(s):  
                    continue

                if i >= 2 and s[0] == '0':
                    continue

                if i >= 3 and int(s[:3]) > 255:
                    continue

                backtrack(address + s[:i] + '.', s[i:], ans, chunk + 1)

        ans = []
        backtrack('', s, ans, 0)
        return ans
        