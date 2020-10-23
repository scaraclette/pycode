def twoSumBinary(arr, target):
  first = 0
  last = len(arr) - 1
  while (first <= last):
    print("first: ", first)
    print("last: ", last)
    comp = arr[first] + arr[last]
    print("comp", comp)
    if comp == target:
      return [first, last]
    elif comp > target:
      last -= 1
    else:
      first += 1

  return []

# print(twoSumBinary([1,2,3,4,6], 6))

# TODO: need to fix
# input: [-2, -1, 0, 2, 3]
def sortedArray(arr):
  negative = 0
  positive = 0
  if arr[0] >= 0:
    pass
  else:
    for i in range(len(arr)):
      if arr[i] > 0:
        positive = i
        negative = i-1
        break

  result = []
  while negative > 0 and positive < len(arr):
    print("postive: ", positive, ", negative: ", negative)
    if arr[negative] < arr[positive]:
      result.append(pow(arr[negative], 2))
      negative -= 1
    else:
      result.append(pow(arr[positive], 2))
      positive += 1
    
  
  while positive < len(arr):
    print("positive:", positive)
    result.append(pow(arr[positive], 2))
    positive += 1
    print(result)
  while negative > 0:
    result.append(pow(arr[negative], 2))
    negative -= 1

  return result

x = 2
print(x != 2)
# print(sortedArray([-2, -1, 0, 2, 3]))
print(sortedArray([1,2,3,4]))
# print(sortedArray([-22, -12, -9, 2, 3, 124, 100]))

