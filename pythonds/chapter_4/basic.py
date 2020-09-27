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