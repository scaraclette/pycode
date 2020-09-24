# CONSECUTIVE 1s
# Given a binary array, find the maximum number of consecutive 1s in this array.
# [1,1,0,1,1,1]
def solution():
    recordCount = 0
    currentCount = 0
    l1 = []
    for i in range(len(l1)):
        if l1[i] == 1:
            currentCount += 1
            if i == len(l1) - 1:
                if currentCount > recordCount:
                    recordCount = currentCount
        else: # number is 0
            if currentCount > recordCount:
                recordCount = currentCount
                currentCount = 0
            else:
                currentCount = 0
    
    print(recordCount)

# FIND NUMBERS WITH EVEN NUMBERS OF DIGITS
# SOLUTION 1 WITH CASTING
def findNumbers():
    nums = [12,345,2,6,7896]
    countEvenDigits = 0
    for i in nums:
        stringNum = str(i)
        if len(stringNum) % 2 == 0:
            countEvenDigits += 1
    
    print(countEvenDigits)

# FIND NUMBERS WITH EVEN NUMBERS OF DIGITS
# SOLUTION 1 WITHOUT CASTING
def findNumbers1():
    nums = [12,345,2,6,7896, 1234543223]
    countEvenDigits = 0
    for i in nums:
        currentCount = 0
        currentNum = i
        while (currentNum != 0):
            currentCount += 1
            currentNum = currentNum // 10
        if currentCount % 2 == 0:
            countEvenDigits += 1
    
    print(countEvenDigits)

# SQUARES OF A SORTED ARRAY
# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order
def sortedSquares():
    A = [-6,-4,-1,0,3,10,11]
    
    # split indexes into two, one to evaluate first positive index and another to evaluate last negative index
    # let i be index for negatives, and j be index for positives
    j = 0
    while j < len(A) and A[j] <= 0:
        j += 1
    i = j-1

    ans = []
    # index through both i and j while evaluating which one is larger
    while i >= 0 and j < len(A):
        if (A[i] ** 2) < (A[j] ** 2):
            ans.append(A[i] ** 2)
            i -= 1
        else:
            ans.append(A[j] ** 2)
            j += 1
    
    # evaluate rest of indexes. Only one loop will be evaluated since there is another that broke the previous while loop condition
    while i >= 0:
        ans.append(A[i] ** 2)
        i -= 1
    while j < len(A):
        ans.append(A[j] ** 2)
        j += 1

    print(ans)

    

sortedSquares()