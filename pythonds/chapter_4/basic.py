class Stack:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def push(self, item):
    # O(1)
    self.items.append(item)

  def pop(self):
    # O(1)
    return self.items.pop()

  def peek(self):
    # O(1)
    return self.items[len(self.items)-1]

  def size(self):
    return len(self.items)

  # returns a reversed string
  def revstring(self, mystr):
    stack = Stack()
    for i in mystr:
      stack.push(i)

    result = ""
    while not stack.isEmpty():
      result += stack.pop()

    return result

'''
      QUEUE
  [rear, ..., ..., ..., front]
'''

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

class Deque:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    return self.items == []

  def addRear(self, item):
    self.items.insert(0, item)

  def addFront(self, item):
    self.items.append(item)

  def removeRear(self):
    return self.items.pop(0)

  def removeFront(self):
    return self.items.pop()

  def size(self):
    return len(self.items)
  