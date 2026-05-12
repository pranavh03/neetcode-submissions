from collections import defaultdict
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)   # add reverse edge for undirected graph

        visited = [False] * n
        count = 0

        def dfs(node):
            if visited[node]:
                return
            visited[node] = True
            for nei in g[node]:
                dfs(nei)

        for i in range(n):
            if not visited[i]:
                dfs(i)       # explore new component
                count += 1   # increment component count

        return count
