from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # Adjacency list representation
        self.V = vertices  # Number of vertices

    def addEdge(self, u, v):
        self.graph[u].append(v)  # Add a directed edge u → v

    def topologicalSortUtil(self, v, visited, stack):
        # Add the current vertex to the 'visited' set
        visited.add(v)

        # Recur for all the neighbors of the current vertex
        for neighbor in self.graph[v]:
            if neighbor not in visited:  # Process unvisited neighbors
                self.topologicalSortUtil(neighbor, visited, stack)

        # Push the current vertex to the stack
        stack.append(v)

    def topologicalSort(self):
        visited = set()  # Set to track visited vertices
        stack = []  # Stack to store the topological order

        # Call the recursive helper function for all unvisited vertices
        for i in range(self.V):
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)

        # Print the stack in reverse order
        print(stack[::-1])


# Example usage
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)
print(Graph)

print("Following is a Topological Sort of the given graph:")
g.topologicalSort()
