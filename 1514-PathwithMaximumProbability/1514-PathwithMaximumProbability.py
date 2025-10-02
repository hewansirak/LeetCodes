# Last updated: 10/2/2025, 10:56:43 PM
import heapq
import math

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:

        graph = [[] for _ in range(n)]
        for (u, v), prob in zip(edges, succProb):
            if prob > 0: 
                log_prob = -math.log(prob) 
                graph[u].append((v, log_prob))
                graph[v].append((u, log_prob))
            else:
                continue 

        heap = [(0.0, start)]  
        
        log_dist = [float('inf')] * n
        log_dist[start] = 0.0
        
        while heap:
            log_prob, node = heapq.heappop(heap)
            
            if node == end:
                return math.exp(-log_prob)
            
            for neighbor, edge_log_prob in graph[node]:
                new_log_prob = log_prob + edge_log_prob  
                
                if new_log_prob < log_dist[neighbor]:
                    log_dist[neighbor] = new_log_prob
                    heapq.heappush(heap, (new_log_prob, neighbor))
        
        return 0.0 

