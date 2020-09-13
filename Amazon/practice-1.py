import collections
# First unique character
def firstUniqeChar(s):
    charDict = {}
    for i in s:
        if i in charDict: # already in dictionary
            addChar = charDict[i] + 1
            charDict[i] = addChar
        else: # not in dictionary
            charDict[i] = 1
    
    # loop through dictionary
    for key, value in charDict.items():
        if value == 1:
            return s.find(key)

    return -1
    
# leet code solution
def firstUniqueCharSol(s):
    # build hash map: character using collections
    count = collections.Counter(s)
    print(count)

    # find index
    for idx, ch in enumerate(s):
        print('idx:', idx, end=" ")
        print('ch:', ch)
        if count[ch] == 1:
            return idx
    
    return -1

print(1 * 10** 9)
