class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        VISITED=2
        UNVISITED=0
        VISITING=1
        g=defaultdict(list)
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)

        States=[UNVISITED]*n
        def dfs(Node,parent):
            state=States[Node]
            if state==VISITING : return False
            if state==VISITED : return True
            States[Node]=VISITING
            for nei in g[Node]:
                if nei==parent:
                    continue
                if not dfs(nei,Node):
                    return False
            States[Node]=VISITED
            return True
        
        if not dfs(0,-1):
            return False
        return all(state==VISITED for state in States)