# Last updated: 11/24/2025, 10:46:34 PM
class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        graph = [[] for _ in range(n)]
        reverse_graph = [[] for _ in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))
            reverse_graph[v].append((u, w))
        
        def dijkstra(start, g):
            dist = [inf] * n
            dist[start] = 0
            heap = [(0, start)]
            
            while heap:
                d, node = heapq.heappop(heap)
                if d != dist[node]:
                    continue
                for neighbor, weight in g[node]:
                    new_dist = d + weight
                    if new_dist < dist[neighbor]:
                        dist[neighbor] = new_dist
                        heapq.heappush(heap, (new_dist, neighbor))
            return dist
        
        # From src1, src2 to all nodes
        dist_from_src1 = dijkstra(src1, graph)
        dist_from_src2 = dijkstra(src2, graph)
        
        # From dest to all nodes
        dist_to_dest = dijkstra(dest, reverse_graph)
        
        # All possible meeting points
        min_weight = inf
        for meeting in range(n):
            if (dist_from_src1[meeting] < inf and 
                dist_from_src2[meeting] < inf and 
                dist_to_dest[meeting] < inf):
                total = dist_from_src1[meeting] + dist_from_src2[meeting] + dist_to_dest[meeting]
                if total < min_weight:
                    min_weight = total
        
        return min_weight if min_weight < inf else -1
