# Last updated: 6/30/2025, 11:35:17 PM
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        for crs, pre in prerequisites:
            adj[crs].append(pre)
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if adj[crs] == []:
                return True

            visited.add(crs)
            for pre in adj[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            adj[crs] = [] 
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True