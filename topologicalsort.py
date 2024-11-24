from collections import defaultdict
class graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=defaultdict(list)
    def addedge(self,u,v):
        self.graph[u].append(v)
    def graphutil(self,visited,stack,u):
        visited.add(u)
        for neighbour in self.graph[u]:
            if neighbour not in visited:
                self.graphutil(visited,stack,neighbour)
        stack.append(u)
    def graphmain(self):
        visited=set()
        stack=[]
        for i in range(self.V):
            if i not in visited:
                self.graphutil(visited,stack,i)
        print(stack[::-1])
g=graph(6)
g.addedge(5,0)
g.addedge(5,2)
g.addedge(4,0)
g.addedge(4,1)
g.addedge(2,3)
g.addedge(3,1)
g.graphmain()