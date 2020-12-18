import unittest
from collections import Counter

# 97
def checkOneOff(shortWord, longWord):
    lenShort, lenLong = 0, 0

    oneOff = False
    while lenShort < len(shortWord) and lenLong < len(longWord):
        if shortWord[lenShort] != longWord[lenLong]:
            if oneOff:
                return False
            oneOff = True
            lenLong += 1
        else:
            lenLong += 1
            lenShort += 1
    
    return True

def checkDiff(word1, word2):
    oneOff = False
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            if oneOff:
                return False
            oneOff = True
    
    return True

def one_away(word1, word2):
    print(word1, word2)
    if len(word1)+1 == len(word2): # word1 is shorter than word2
        return checkOneOff(word1, word2)
    elif len(word1)-1 == len(word2): # word2 is shorter than word1
        return checkOneOff(word2, word1)
    elif len(word1) == len(word2):
        return checkDiff(word1, word2)
    
    return False

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('pale', 'ple', True),
        ('pales', 'pale', True),
        ('pale', 'bale', True),
        ('paleabc', 'pleabc', True),
        ('pale', 'ble', False),
        ('a', 'b', True),
        ('', 'd', True),
        ('d', 'de', True),
        ('pale', 'pale', True),
        ('pale', 'ple', True),
        ('ple', 'pale', True),
        ('pale', 'bale', True),
        ('pale', 'bake', False),
        ('pale', 'pse', False),
        ('ples', 'pales', True),
        ('pale', 'pas', False),
        ('pas', 'pale', False),
        ('pale', 'pkle', True),
        ('pkle', 'pable', False),
        ('pal', 'palks', False),
        ('palks', 'pal', False)
    ]

    def test_one_away(self):
        for [test_s1, test_s2, expected] in self.data:
            actual = one_away(test_s1, test_s2)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()