# Last updated: 8/28/2025, 11:58:56 PM
class UnionFind:
    def __init__(self, size):
        self.parent = [node for node in range(size)]
        self.rank = [1 for _ in range(size)]
    def find(self, node):
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
  
        if self.rank[rx] < self.rank[ry]:
            self.parent[rx] = ry
        elif self.rank[rx] > self.rank[ry]:
            self.parent[ry] = rx
        else:
            self.parent[ry] = rx
            self.rank[rx] += 1
        

class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        union_find = UnionFind(n)
        ans = []
        
        for u, v in requests:
            #  finding the group on which u, v blog
            #  we are planning to create fre gu - gv
            #  gu, gv
            is_valid = True

            root_u, root_v = union_find.find(u), union_find.find(v)
            for ur, vr in restrictions:
                root_ur, root_vr = union_find.find(ur), union_find.find(vr)
                #  1, 2  or 2, 1
                if sorted([root_ur, root_vr]) == sorted([root_u, root_v]):
                    is_valid = False
                    break
            if is_valid:
                union_find.union(u, v)
                ans.append(True)
            else:
                ans.append(False)
        return ans
