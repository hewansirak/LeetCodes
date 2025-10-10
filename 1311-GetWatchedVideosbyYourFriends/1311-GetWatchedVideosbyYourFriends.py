# Last updated: 10/11/2025, 12:00:50 AM
class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        
        n = len(friends)
        
        queue = deque([id])
        visited = {id}
        degree = 0

        while queue:
            size = len(queue)
            if degree == level:
                break
            
            for _ in range(size):
                curInd = queue.popleft()
                for nextInd in friends[curInd]:
                    if nextInd not in visited:
                        visited.add(nextInd)
                        queue.append(nextInd)
            degree += 1
        
        freq = defaultdict(int)
        
        for q in queue:
            for v in watchedVideos[q]:
                freq[v] += 1
        
        
        s = sorted(freq.items(), key=lambda kv: (kv[1], kv[0]))
        return [i for i,_ in s]
