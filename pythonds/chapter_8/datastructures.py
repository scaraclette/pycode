# VERTEX class to represent each vertex in the graph
class Vertex:
  def __init__(self, key):
    self.id = key
    self.connectedTo = {}
    # Additional fields for BFS
    self.pred = None
    self.color = 'black'
    self.distance = 0

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

  # ADDITIONAL FIELDS
  def setDistance(self, nd):
    self.distance = nd
  def setPred(self, p):
    self.pred = p
  def setColor(self, c):
    self.connectedTo = c
  def getDistance(self):
    return self.distance
  def getPred(self):
    return self.pred
  def getColor(self):
    return self.color

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

# QUEUE
class Queue:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def enqueue(self, item):
    self.items.insert(0, item)

  def dequeue(self):
    return self.items.pop()

  def size(self):
    return len(self.items)