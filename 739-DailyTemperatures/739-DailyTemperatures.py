# Last updated: 4/27/2025, 10:58:57 PM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        ans = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev = stack.pop()

                ans[prev] = i - prev

            stack.append(i)

        return ans