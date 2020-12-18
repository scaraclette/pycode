import math
# Simple binary search find target at index
def binarySearch(someList, target):
  low = 0
  high = len(someList) - 1
  while low <= high:
    mid = (high+low)//2
    if someList[mid] == target:
      return mid

    if target > mid:
      low = mid+1
    else:
      high = mid-1
  
  return -1

# Use binary search to find min
# 7, 8. 9, 20. 1, 2, 3
def findMin(someList):
  if len(someList) == 1:
    return someList[0]

  low = 0
  high = len(someList) - 1
  while (low <= high):
    mid = low + (high - low) // 2
    if someList[mid] > someList[mid+1]:
      return someList[mid+1]
    if someList[mid] < someList[mid-1]:
      return someList[mid]

    if someList[high] < someList[mid]:
      low = mid + 1
    else:
      high = mid - 1

  return someList[mid]

# l = [1, 2, 3, 4, 5, 7, 8, 9, 10], 6
def findCeil(someList, key):
  low = 0
  high = len(someList) - 1
  while (low <= high):
    mid = (low + high) // 2
    if someList[mid] == key:
      return mid
    if someList[mid] >= key and someList[mid-1] < key:
      return mid
    # move mid
    if key > someList[mid]:
      low = mid+1
    else:
      high = mid - 1

  return -1

def squareIt(num):
  low = 0
  high = num
  while (low <= high):
    print("low: ", low, "high: ", high)
    mid = (low + high) // 2
    print("mid: ", mid)
    if mid * mid == num:
      return mid
    if mid * mid > num:
      high = mid - 1
    else:
      low = mid + 1

  # low = 0
  # high = num
  # while (low <= high):
  #   print("low: ", low, "high: ", high)
  #   mid = (low + high) / 2
  #   print("mid: ", mid)
  #   if mid * mid == num:
  #     return mid
  #   if mid * mid > num:
  #     high = mid - 1
  #   else:
  #     low = mid + 1

  return mid


def find_ceiling(arr, key):
  n = len(arr)
  if key > arr[n-1]:
    return -1

  left, right = 0, n - 1
  while left <= right:
    mid = (left + right) // 2
    if key < arr[mid]:
      right = mid - 1
    elif key > arr[mid]:
      left = mid + 1
    return mid
  return left

def searchSorted(nums, target):
  low = 0
  high = len(nums) - 1
  while (low <= high):
    mid = (low + high) // 2
    if (nums[mid] == target):
      return mid
    if (target < nums[mid]):
      high = mid-1
    else:
      low = mid+1
  
  return -1


def client_binarySearch():
  # l = [1,2,5,6,78,99]
  # l = [1, 2, 3, 4, 5, 7, 8, 9, 10]
  # l2 = [1, 2, 3, 4, 5]
  # l3 = [-1,1,2,3]
  # print(findCeil(l, 6))
  # print(findCeil(l3, 6))
  # print(binarySearch(l, 78))
  # num = 8
  # print("result wanted: ", math.sqrt(num))
  # print(squareIt(num))
  nums = [4, 5, 6, 7, 8, 0, 1, 2, 3]
  searchSorted(nums, 3)


client_binarySearch()