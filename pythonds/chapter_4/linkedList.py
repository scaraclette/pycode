class Node:
  def __init__(self, initdata):
    self.data = initdata
    self.next = None

  def getData(self):
    return self.data

  def getNext(self):
    return self.next

  def setData(self, newdata):
    self.data = newdata

  def setNext(self, newnext):
    self.next = newnext

# UNORDERED LIST 
class UnorderedList:
  def __init__(self):
    self.head = None
    self.count = 0
    self.tail = self.head

  def isEmpty(self):
    return self.head == None

  # O(1)
  def add(self, item):
    newNode = Node(item)
    if self.head == None:
      self.tail = newNode
    newNode.setNext(self.head)
    self.head = newNode
    self.count += 1
  
  # O(n) TODO: fix to O(1)
  # Alternatively, it's addLast method
  def append(self, item):
    newNode = Node(item)
    # if head is none, just add the item/set it to head
    if self.head == None:
      self.head = self.tail = newNode
      self.count += 1
      return
    self.tail.setNext(newNode)
    self.tail = newNode
    self.count += 1

  # O(n), alternatively create a pointer for size which becomes O(1)
  def size(self):
    return self.count

  def search(self, item):
    current = self.head
    found = False
    while current != None and not found:
      if current.getData() == item:
        found = True
      else:
        current = current.getNext()

    return found

  # TODO: fix tail/head
  # O(n)
  def remove(self, item):
    current = self.head
    previous = None
    found = False
    while not found:
      # Handle end of current/item not found
      if current == None:
        return False
      # item found
      if current.getData() == item:
        found = True
        if current == self.tail:
          # Tail was removed, set tail to previous Node
          self.tail = previous
      else:
        previous = current
        current = current.getNext()

    if previous == None:
      self.head = current.getNext()
    else:
      previous.setNext(current.getNext())
      self.count -= 1
  
  def __str__(self):
    result = ""
    current = self.head
    while current != None:
      result += '-' + str(current.getData())
      current = current.getNext()
    
    return result + '-x'

def clientUnorderedList():
  mylist = UnorderedList()
  mylist.add(1)
  mylist.add(2)
  mylist.add(3)
  mylist.add(4)
  mylist.add(5)
  mylist.append(69)
  print(mylist)
  mylist.remove(69)
  print(mylist)
  mylist.append(3)
  print(mylist)
  print(mylist.remove(343)) # BROKEN

clientUnorderedList()

# ORDERED LIST
class OrderedList:
  def __init__(self):
    self.head = None

  def search(self, item):
    current = self.head
    found = False
    stop = False
    while current != None and not found and not stop:
      if current.getData() == item:
        found = True
      else:
        if current.getData() > item:
          stop = True
        else:
          current = current.getNext()
    
    return found
  
  def add(self, item):
    current = self.head
    previous = None
    stop = False
    while current != None and not stop:
      if current.getData() > item:
        stop = True
      else:
        previous = current
        current = current.getNext()

    temp = Node(item)
    if previous == None:
      temp.setNext(self.head)
      self.head = temp
    else:
      temp.setNext(current)
      previous.setNext(temp)
    
  def isEmpty(self):
    return self.head == None
  
  # Can be improved O(n) -> O(1)
  def size(self):
    current = self.head
    count = 0
    while current != None:
      count = count + 1
      current = current.getNext()
    
    return count