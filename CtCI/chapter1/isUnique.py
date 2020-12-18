# implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

# Without additional datastructure. O(n^2)
def isUnique(word):
    for i in range(len(word)-1):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False
    return True

# Without additional datastructure, O(n)
def isUnique1(word):
    checker = 0
    for i in range(len(word)):
        bitAtIndex = ord(word[i]) - ord('a')

        if ((bitAtIndex) > 0):
            if ((checker & ((1 << bitAtIndex)))):
                return False
            
            checker = checker | (1 << bitAtIndex)
    
    return True


# With additional datastructure
def isUnique2(word):
    result = set([i for i in word])
    return len(result) == len(word)


def main():
    word = "helo"
    print(isUnique1(word))

main()