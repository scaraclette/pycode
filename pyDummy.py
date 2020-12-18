from collections import defaultdict

def main():
  # paths = [['B', 'A'], ['C', 'A'], ['D', 'A'], ['A', 'F']]
  paths = [['A', 'B'], ['A', 'C'], ['B', 'K'], ['C', 'K'], ['E', 'L'], ['F', 'G'], ['J', 'M'], ['E', 'F'], ['G', 'H'], ['G', 'I']]

  # Creating path dict
  pathDict = defaultdict(list)
  for i in range(len(paths)):
    pathDict[paths[i][0]].append(paths[i][1])

  # Adding all values
  values = set()
  for member in paths:
    values.add(member[1])

  # Get roots
  roots = []
  for key in pathDict:
    if (key not in values):
      roots.append(key)

  # DFS traverse to find ends
  result = defaultdict(list)

  print("DFS")
  for r in roots:
    stack = [r]
    # print("stack: ", stack)
    visited = set()
    # print("\n")
    while stack:
      current = stack.pop()
      if (current in visited):
        continue
      
      # check if end
      if current not in pathDict:
        result[r].append(current)
      print("root: %s, current: %s" % (r, current))
      visited.add(current)
      if pathDict.get(current):
        for val in pathDict[current]:
          stack.append(val)

    print(result)
      

  # result = {}

  # while(not stack):
  #   current = stack.pop()
  #   if (current not in pathDict):
  #     result[]

  


main()