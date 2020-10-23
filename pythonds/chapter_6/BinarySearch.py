def binarySearchRecursion(arr, first, last, target):
  index = 0
  if (first > last):
    return -1
  
  mid = first + (last - first) // 2
  if (arr[mid] == target):
    return mid
  if (target > arr[mid]):
    index = binarySearchRecursion(arr, mid + 1, last, target)
  else:
    index = binarySearchRecursion(arr, first, mid - 1, target)

  return index

def binarySearchIterative(arr, target):
  first = 0
  last = len(arr) - 1
  while first <= last:
    mid = first + (last-first)//2
    if arr[mid] == target:
      return mid
    if target > arr[mid]:
      first = mid + 1
    else:
      last = mid - 1
  
  return -1

def findMaxRecursion(arr):
  if len(arr) == 1:
    return arr[0]
  else:
    mid = len(arr) // 2
    return max(findMaxRecursion(arr[:mid]), findMaxRecursion(arr[mid:]))
  

def findMaxBSIterative(arr):
  first = 0
  last = len(arr) - 1
  maxNum = float('-inf')
  while (first <= last):
    pass

  return maxNum

def main():
  arr = [3,2,53,23,6443,123,54]
  

main()