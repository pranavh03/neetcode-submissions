#from collections import defaultDict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g=defaultdict(list)
        courses=prerequisites
        for i,j in courses:
            g[i].append(j)
        VISITED=2
        VISITING=1
        UNVISITED=0
        states=[UNVISITED]*numCourses

        def dfs(Node):
            state=states[Node]
            if state==VISITING :return False
            elif state==VISITED : return True

            states[Node]=VISITING

            for nei in g[Node]:
                if not dfs(nei):
                    return False
            states[Node]=VISITED
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        