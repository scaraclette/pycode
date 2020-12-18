# VERTEX class to represent each vertex in the graph
class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {}

  def addNeighbor (self, nbr, weight = 0):
    self.connectedTo[nbr] = weight

  def __str__(self):
    return str(self.id) + " connectedTo: " + str([x.id for x in self.connectedTo])

  def getConnections(self):
    return self.connectedTo.keys()

  def getId(self):
    return self.id

  def getWeight(self, nbr):
    return self.connectedTo[nbr]

# GRAPH class holds the master list of vertices
class Graph:
  def __init__(self):
    self.vertList = {}
    self.numVertices = 0

  def addVertex(self, key):
    self.numVertices = self.numVertices + 1
    newVertex = Vertex(key)
    # printing vertlist will give the key: object address
    self.vertList[key] = newVertex
    return newVertex

  def getVertex(self, n):
    if n in self.vertList:
      return self.vertList[n]
    else:
      return None

  def __contains__(self, n):
    return n in self.vertList

  # Add edge, from one v to another v with default weight 0
  def addEdge(self, fromV, toV, weight = 0):
    if fromV not in self.vertList:
      self.addVertex(fromV)
    if toV not in self.vertList:
      self.addVertex(toV)
    self.vertList[fromV].addNeighbor(self.vertList[toV], weight)

  def getVertices(self):
    return self.vertList.keys()

  def getNumVertices(self):
    return self.numVertices

  def __iter__(self):
    return iter(self.vertList.values())

  def printGraph(self):
    for v in self.vertList:
      # print("%s (id: %s): %s" % (v, id(self.vertList[v]), self.vertList[v]))
      print(self.vertList[v])

def test_graph():
  g = Graph()
  for i in range(6):
    g.addVertex(i)
  # print("We are printing the vertList:")
  # print(g.vertList)
  print("Total vertices:", g.numVertices)
  # ADDING EDGES
  g.addEdge(0, 1, 5)
  g.addEdge(0,5,2)
  g.addEdge(1,2,4)
  g.addEdge(2,3,9)
  g.addEdge(3,4,7)
  g.addEdge(3,5,3)
  g.addEdge(4,0,1)
  g.addEdge(5,4,8)
  g.addEdge(5,2,1)
  g.printGraph()
  for v in g:
    print("Current v: ", v.getId())
    for w in v.getConnections():
      print("( %s, %s )" % (v.getId(), w.getId()))

test_graph()