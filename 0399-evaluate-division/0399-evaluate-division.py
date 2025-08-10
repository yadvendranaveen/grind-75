class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (u,v), value in zip(equations, values):
            graph[u][v] = value
            graph[v][u] = 1/value
        def bfs(start, target):
            if start not in graph or target not in graph:    return -1.0
            if start==target:    return 1.0
            q = deque([(start, 1.0)])
            visited = set()
            while q:
                node, curr = q.popleft()
                if node == target:  return curr
                visited.add(node)
                for k,v in graph[node].items():
                    if k not in visited:
                        q.append((k, curr*v))
            return -1.0
        return [bfs(start, target) for start, target in queries]

                
            