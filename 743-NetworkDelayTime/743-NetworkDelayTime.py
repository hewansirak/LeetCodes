# Last updated: 9/30/2025, 11:26:42 PM
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, time in times:
            graph[u].append([v, time])
        
        time_needed = [float('inf')] * n
        time_needed[k-1] = 0
        heap = [[0, k]] 

        visited = set() 
        visited.add(k)

        while heap: 
            time, cur_node = heappop(heap)
            for nei, nei_time in graph[cur_node]:
                total_time = time + nei_time
                if total_time < time_needed[nei-1]:
                    time_needed[nei-1] = total_time
                    visited.add(nei)
                    heappush(heap, [total_time, nei])

        return max(time_needed) if len(visited) == n else -1