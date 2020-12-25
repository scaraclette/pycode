from collections import deque

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight = 0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getWeight(self, nbr):
        return self.connectedTo[nbr]

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex
    
    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList
    
    def addEdge(self, f, t, weight = 0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def bfs(self, start):
        visited = [False] * (max(self.vertList) + 1)
        print(visited)

        dq = deque()
        dq.append(start)
        visited[start] = True

        while dq:
            current = dq.popleft()
            print(current, end=", ")

            for i in self.vertList[current].getConnections():
                currentId = i.id
                if visited[currentId] == False:
                    dq.append(currentId)
                    visited[currentId] = True
        
        print()

if __name__=="__main__":
    g = Graph()
    for i in range(6):
        g.addVertex(i)
    g.addVertex(9)
    print(g.vertList)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    g.addEdge(9,5,1)
    g.addEdge(5,9,1)
    for v in g:
        print(v)
    g.bfs(1)
