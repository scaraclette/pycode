import unittest

# Implement an algorithm to determine if a string has all unique characters. Don't use additional data structures.
def isUnique(word):
    # O(n^2)
    for i in range(len(word)):
        for j in range(i+1, len(word)):
            if word[i] == word[j]:
                return False

    return True

# Also isUnique but this one takes an extra space
def isUnique1(word):
    # O(n)
    # Let characters be ascii
    char_set = [False for _ in range(128)]
    for w in word:
        # character to ascii value
        if char_set[ord(w)]:
            return False
        else:
            char_set[ord(w)] = True
    
    return True

class Test(unittest.TestCase):
    dataT = [('abcd'), ('s4fad'), ('')]
    dataF = [('23ds2'), ('hb 627jh=j ()')]

    def test_unique(self):
        # true check
        for test_string in self.dataT:
            actual = isUnique1(test_string)
            self.assertTrue(actual)
        # false check
        for test_string in self.dataF:
            actual = isUnique1(test_string)
            self.assertFalse(actual)

if __name__=="__main__":
    unittest.main()
