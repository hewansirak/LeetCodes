# Last updated: 7/24/2025, 9:19:41 PM
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer = 0
        count = defaultdict(int)
        for val in answers:
            if count[val] > val:
                count[val] = 0
            if not count[val]:
                answer += val + 1
            count[val] += 1
        return answer