# Last updated: 4/1/2025, 10:44:00 PM
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(math.sqrt(c))
        while left <= right:
            if left * left + right * right == c:
                return True
            elif left * left + right * right > c:
                right -= 1
            else:
                left += 1
        return False