import unittest
from collections import Counter

def palindromePermutation(string):
  print('STRING:', string)
  stringList = sorted(string.replace(' ', '').lower())
  print(stringList)
  stringDict = {}
  for i in stringList:
    if i not in stringDict:
      stringDict[i] = 1
    else:
      if stringDict[i] == 0:
        stringDict[i] += 1
      else:
        stringDict[i] -= 1

  isEven = len(stringList) % 2 == 0
  singleLetter = False
  print('stringDict:', stringDict)
  for key in stringDict:
    if stringDict[key] < 0 or (stringDict[key] == 1 and isEven) or (stringDict[key] == 1 and singleLetter):
      return False

    if stringDict[key] == 1:
      if not isEven:
        singleLetter = True
      else:
        return False
    
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
            actual = palindromePermutation(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
