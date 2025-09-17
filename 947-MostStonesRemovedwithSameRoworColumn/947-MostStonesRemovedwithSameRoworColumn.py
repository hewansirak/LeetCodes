# Last updated: 9/17/2025, 11:31:07 PM
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        parent = {}

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)

        offset = 10001 
        for r, c in stones:
            union(r, c + offset)

        roots = set(find(r) for r, _ in stones)
        return len(stones) - len(roots)