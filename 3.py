from collections import defaultdict
class graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfsutility(self,u,visited):
        visited.add(u)
        print(u,end=" ")
        for neighbour in self.graph[u]:
            if neighbour not in visited:
                self.dfsutility(neighbour,visited)
    def dfs(self,u):
        visited=set()
        self.dfsutility(u,visited)
g=graph()
g.addEdge(0, 1)  
g.addEdge(0, 2)  
g.addEdge(1, 2)  
g.addEdge(2, 0)  
g.addEdge(2, 3)  
g.addEdge(3, 3)  
print("Following is DFS from (starting from vertex 2)")  
g.dfs(2) 