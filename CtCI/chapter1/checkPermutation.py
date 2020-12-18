from collections import Counter
# Check permutation: Given two strings, write a method to decide if one is a
# permutation of the other

def checkPermutation(word1, word2):
    if len(word1) != len(word2):
        return False
    
    result1 = set([i for i in word1])
    result2 = set([i for i in word2])

    print(result1)
    print(result2)

    return result1 == result2

def checkPermutation2(word1, word2):
    if len(word1) != len(word2):
        return False
    w1 = [i for i in word1]
    print(w1)
    w2 = [i for i in word2]
    print(w2)

    w1.sort()
    w2.sort()

    for i in range(len(w1)):
        if w1[i] != w2[i]:
            return False
    
    return True

def checkPermutation3(word1, word2):
    # Using dictionary
    count = Counter()
    for i in word1:
        count[i] += 1
    for j in word2:
        if count[j] == 0:
            return False
        count[j] -= 1

    return True



print(checkPermutation3("word", "dwor"))
