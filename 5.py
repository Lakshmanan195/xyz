from collections import defaultdict
class graph:
    def __init__(self,value):
        self.graph=defaultdict(list)
        self.V=value
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def topo_util(self,v,visited,stack):
        visited.add(v)
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.topo_util(neighbour,visited,stack)
        stack.append(v)
    def main_topo(self):
        visited=set()
        stack=[]
        for i in range(self.V):
            if i not in visited:
                self.topo_util(i,visited,stack)
        print(stack[::-1])
g = graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)


print("Following is a Topological Sort of the given graph:")
g.main_topo()