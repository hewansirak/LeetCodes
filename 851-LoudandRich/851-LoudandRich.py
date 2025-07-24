# Last updated: 7/24/2025, 11:22:54 PM
class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        g = defaultdict(list)
        incoming = defaultdict(int)

        for v, u in richer:
            g[v].append(u)
            incoming[u] += 1

        q = deque([])

        for i in range(n):
            if incoming[i] == 0:
                q.append(i)

        ans = [i for i in range(n)]

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                for child in g[node]:
                    incoming[child] -= 1

                    if incoming[child] == 0:
                        q.append(child)

                    print(ans[child])

                    if quiet[ans[node]] < quiet[ans[child]]:
                        ans[child] = ans[node]
        return ans