# HAPPY NUMBER
# Write an algorithm to determine if a number n is "happy".
# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
# Return True if n is a happy number, and False if not.
def isHappy(n):
    checkNums = {}
    while (n != 1):
        currentSum = 0
        while (n != 0):
            currentSum += (n % 10) ** 2
            n = n // 10
        n = currentSum

        if n in checkNums: # Number already exists in dictionary and will therefore loop again
            return False
        else: # add new number in dictionary
            checkNums[n] = n

# VALID PARENTHESES
def isValid(s):
    # example: (({})){}[]()
    stack = []
    checkClosing = {")":"(", "}":"{", "]":"["}

    for i in s:
        if i not in checkClosing: # open bracket
            stack.append(i)
        else: # closing bracket
            currentTop = stack.pop()
            if checkClosing[i] != currentTop:
                return False     

    return stack == []

# print(isValid('()'))

s = 'hello'
print(s[:2])