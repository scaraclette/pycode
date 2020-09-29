from basic import Deque

def palchecker(aString):
  chardeque = Deque()

  for ch in aString:
    # addRear results to O(n), using addFront is O(1) and wouldn't matter what the position is since it's just a checker
    # chardeque.addRear(ch)
    chardeque.addFront(ch)

  while chardeque.size() > 1 and not chardeque.isEmpty():
    first = chardeque.removeFront()
    last = chardeque.removeRear()
    if first != last:
      return False
    
    return True

print(palchecker("lsdkjfskf"))
print(palchecker("radar"))
