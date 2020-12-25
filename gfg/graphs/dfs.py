from collections import defaultdict

# Directed graph using adjacency list representation
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def _dfs(self, v, visited):
        visited.add(v)
        print(v, end=' ')

        # Recur for all the vertices adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self._dfs(neighbour, visited)

    def dfs(self, v):
        # Create a set to store visited vertices
        visited = set()

        # Call the recursive helper to print DFS traversal
        self._dfs(v, visited)

if __name__=="__main__":
    # Create a graph given
    # in the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    
    print("Following is DFS from (starting from vertex 2)")
    g.dfs(2)
    