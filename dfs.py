from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def dfs(self,u):
        visited.add(u)
        print(u)
        for neighbour in self.graph[u]:
            if neighbour not in visited:
                self.dfs(neighbour)
visited=set()
g=graph()
g.addedge(0,1)
g.addedge(0,2)
g.addedge(2,0)
g.addedge(1,2)
g.addedge(2,3)
g.dfs(2)

