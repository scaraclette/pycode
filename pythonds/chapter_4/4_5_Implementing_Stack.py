class StackReverse:
  def __init__(self):
    self.items = []

  def isEmpty(self):
    # O(1)
    return self.items == []

  def push(self, item):
    # O(n)
    self.items.insert(0, item)

  def pop(self):
    # O(n)
    return self.items.pop(0)

  def peek(self):
    # O(1)
    return self.items[0]

  def size(self):
    return len(self.items)

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

def parChecker(symbolString):
  s = Stack()
  balanced = True
  index = 0

  while index < len(symbolString) and balanced:
    symbol = symbolString[index]
    if symbol == "(": # is opening bracket
      s.push(symbol)
    else:
      if s.isEmpty:
        balanced = False
      else:
        s.pop()

    index += 1

  if balanced and s.isEmpty():
    return True
  else:
    return False

def parChecker1(symbolString):
  s = Stack()
  dictP = {")":"(", "}":"{", "]":"["}
  for i in symbolString:
    if i not in dictP:
      s.push(i)
    else:
      if not s.isEmpty():
        popped = s.pop()
        if dictP[i] != popped:
          return False

  return s.isEmpty()

def decToBin(number):
  stack = Stack()
  while number > 0:
    stack.push(number % 2)
    number = number // 2

  return stack

def main():
  binResult = decToBin(256)
  result = ""
  while not binResult.isEmpty():
    result += str(binResult.pop())

  print(result)

main()