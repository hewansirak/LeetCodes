# Last updated: 9/7/2025, 9:12:15 PM
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
        
        answer = [""] * n
        
        for i, (idx, _) in enumerate(sorted_scores):
            if i == 0:
                answer[idx] = "Gold Medal"
            elif i == 1:
                answer[idx] = "Silver Medal"
            elif i == 2:
                answer[idx] = "Bronze Medal"
            else:
                answer[idx] = str(i + 1) 
        return answer