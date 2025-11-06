# Last updated: 11/6/2025, 11:42:42 PM
class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:

        n = len(source)
        if len(target) != n:
            return -1

        ALPHA = 26
        def idx(ch: str) -> int:
            return ord(ch) - ord('a')

        adj = [[] for _ in range(ALPHA)]

        min_edge = {}
        for o, c, w in zip(original, changed, cost):
            u = idx(o)
            v = idx(c)
        
            # minimum edge weight 
            if (u, v) not in min_edge or w < min_edge[(u, v)]:
                min_edge[(u, v)] = w
        for (u, v), w in min_edge.items():
            adj[u].append((v, w))

        # for each source char
        needed_sources = set()
        for i in range(n):
            if source[i] != target[i]:
                needed_sources.add(idx(source[i]))

        def dijkstra(start: int):
            INF = 10**18
            dist = [INF] * ALPHA
            dist[start] = 0
            heap = [(0, start)]
            while heap:
                d, u = heapq.heappop(heap)
                if d != dist[u]:
                    continue
                for v, w in adj[u]:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heapq.heappush(heap, (nd, v))
            return dist

        # Cache distances
        dist_cache = {}
        for s in needed_sources:
            dist_cache[s] = dijkstra(s)

        total = 0
        INF = 10**18
        for i in range(n):
            a = idx(source[i])
            b = idx(target[i])
            if a == b:
                continue
            dist_ab = dist_cache.get(a)

            if dist_ab is None:
                dist_ab = dijkstra(a)
                dist_cache[a] = dist_ab
            if dist_ab[b] >= INF:
                return -1
            total += dist_ab[b]

        return total
