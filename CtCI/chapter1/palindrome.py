import unittest
from collections import Counter

def pal_perm(word):
    letterCount = Counter()
    for i in word:
        if i.isalnum():
            letterCount[i.lower()] += 1
    
    isOdd = False
    for i in letterCount:
        if isOdd and letterCount[i] % 2 != 0:
            return False
        if letterCount[i] % 2 != 0:
            isOdd = True

    return True

class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('Tact Coa', True),
        ('jhsabckuj ahjsbckj', True),
        ('Able was I ere I saw Elba', True),
        ('So patient a nurse to nurse a patient so', False),
        ('Random Words', False),
        ('Not a Palindrome', False),
        ('no x in nixon', True),
        ('azAZ', True)]

    def test_pal_perm(self):
        for [test_string, expected] in self.data:
            actual = pal_perm(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()