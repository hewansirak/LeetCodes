# Last updated: 4/2/2025, 10:14:20 PM
class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        starts = sorted([(s, i) for i, (s, e) in enumerate(intervals)], key=itemgetter(0))
        ends = sorted([(e, i) for i, (s, e) in enumerate(intervals)], key=itemgetter(0))
        res = [-1 for _ in range(n)]
        sidx = 0
        for end in ends:
            e, i = end
            while starts[sidx][0]<e and sidx+1<n:
                    sidx += 1
            if starts[sidx][0] < e:
                break
            else:
                res[i] = starts[sidx][1]
        return res        
        