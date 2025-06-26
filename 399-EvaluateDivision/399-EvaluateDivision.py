# Last updated: 6/26/2025, 9:35:43 PM
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for i in range(len(equations)):
            numerator, denominator = equations[i]
            value = values[i]
            graph[numerator][denominator] = value
            graph[denominator][numerator] = 1 / value

        results = []
        for query_num, query_den in queries:
            visited = set()
            result = self.dfs(query_num, query_den, visited, 1.0, graph)
            results.append(result)
        return results

    def dfs(self, source: str, dest: str, visited: set, value: float, graph: dict) -> float:
        if source not in graph or dest not in graph:
            return -1

        if source == dest:
            return value

        visited.add(source)

        for neighbor, weight in graph[source].items():
            if neighbor in visited:
                continue

            temp = self.dfs(neighbor, dest, visited, value * weight, graph)

            if temp != -1:
                return temp

        return -1