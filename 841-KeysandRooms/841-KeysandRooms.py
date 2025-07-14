# Last updated: 7/14/2025, 10:18:42 PM
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        visited = [False] * n
        
        queue = collections.deque()
        visited[0] = True
        queue.append(0)
        
        count = 1 
        
        while queue:
            curr = queue.popleft() 
            
            for key in rooms[curr]:
                if not visited[key]:
                    visited[key] = True 
                    count += 1 
                    queue.append(key)    
        
        return count == n
