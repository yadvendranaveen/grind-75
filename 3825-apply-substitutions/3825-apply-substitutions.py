class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:

        def substitute(s, flat_replacements):
            for key, value in flat_replacements:
                s = s.replace(f"%{key}%", value)
            return s
        d = dict(replacements)
        graph = defaultdict(list)
        for u, v in replacements:
            graph[u] = re.findall(r"%([A-Z])%", v)
        
        visited = set()
        def dfs(node):
            if node in visited: return d[node]
            visited.add(node)

            curr_replacements = []
            for neighbor in graph[node]:
                curr_replacements += [ (neighbor, dfs(neighbor)) ]

            substituted_str = substitute(d[node], curr_replacements)
            d[node] =  substituted_str
            return d[node]

        for node,_ in replacements:
            dfs(node)
        return substitute(text, d.items())

            

