class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n<=2:    return [i for i in range(n)]

        graph=defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        leaves = [i for i in range(n) if len(graph[i])==1]

        remainingNodes = n
        while remainingNodes>2:
            remainingNodes-=len(leaves)
            newLeaves = []
            while leaves:
                leaf=leaves.pop()
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor])==1:
                    newLeaves.append(neighbor)
                
            leaves = newLeaves
        return leaves

        