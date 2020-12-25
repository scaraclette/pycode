"""
Python3 program to print BFS traversal
from a given source vertex. BFS (int s) 
traverses vertices reachable from s.
"""
from collections import defaultdict, deque

# This class represents a DIRECTED graph
# using adjency list representation
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        # max(self.graph) + 1 prints the largest node + 1 in graph
        visited = [False] * (max(self.graph) + 1)

        # Create a queue for BFS
        dq = deque()

        # Mark the source node as visited and enqueue it
        dq.append(s)
        visited[s] = True

        while dq:
            # Dequeue a vertex from queue and print it
            # TODO: might need to change pop
            s = dq.popleft()
            print(s, end=" ")

            # Get all adjacent vertices of the
            # dequeued vertex s. If an adjacent
            # has not been visited, then mark it visited
            # and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    dq.append(i)
                    visited[i] = True

    def printDict(self):
        print(self.graph)


if __name__=="__main__":
    g = Graph()
    # g.addEdge(0, 1)
    # g.addEdge(0, 2)
    # g.addEdge(1, 2)
    # g.addEdge(2, 0)
    # g.addEdge(2, 3)
    # g.addEdge(3, 3)
    g.addEdge(1,5)
    g.addEdge(5,3)
    g.addEdge(3,2)
    g.addEdge(2,4)
    g.addEdge(4,3)
    g.printDict()
    print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
    g.BFS(1)
    print()

