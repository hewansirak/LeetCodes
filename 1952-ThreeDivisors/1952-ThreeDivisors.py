# Last updated: 9/11/2025, 11:41:59 PM
class Solution:
    def isThree(self, n: int) -> bool:
        divs = set()
        for i in range(1, n+1):
            if n%i == 0:
                divs.add(i)
            if len(divs) > 3:
                return False
        return len(divs) == 3