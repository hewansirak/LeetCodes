# Last updated: 6/25/2025, 10:58:19 PM
class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(index, prev):
            if index == len(s):
                return True  # Successfully split entire string

            for i in range(index + 1, len(s) + 1):
                num = int(s[index:i])
                if num == prev - 1:
                    if backtrack(i, num):
                        return True
            return False

        for i in range(1, len(s)):
            first = int(s[:i])
            if backtrack(i, first):
                return True

        return False