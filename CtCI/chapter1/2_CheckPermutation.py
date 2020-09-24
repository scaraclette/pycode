import unittest
from collections import Counter

# Given two strings, write a method to decide if one is a permutation of the other
def checkPermutation(word1, word2):
    # O(n)
    # simple length check
    if len(word1) != len(word2):
        return False

    wordDict = {}
    for i in word1:
        if i not in wordDict:
            wordDict[i] = 1
        else:
            wordDict[i] = wordDict[i] + 1
    
    for i in word2:
        if i not in wordDict:
            return False
        wordDict[i] = wordDict[i] + 1

    for key in wordDict:
        if wordDict[key] % 2 != 0:
            return False

    return True

# SOLUTION
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

class Test(unittest.TestCase):
    words1 = ['si', 'is']
    words2 = ['deno', 'node']
    dataT = (
        ('abcd', 'bacd'),
        ('3563476', '7334566'),
        ('wef34f', 'wffe34'),
    )
    dataF = (
        ('abcd', 'd2cba'),
        ('2354', '1234'),
        ('dcw4f', 'dcw5f'),
    )

    def customTest1(self):
        # true check
        result1 = checkPermutation(self.words1[0], self.words1[1])
        self.assertTrue(result1)
        result2 = checkPermutation(self.words2[0], self.words2[1])
        self.assertTrue(result2)

    def customTest2(self):
        # false check
        result = checkPermutation('chonky', 'dendot')
        self.assertFalse(result)

    def test_cp(self):
        # true check
        for test_strings in self.dataT:
            result = checkPermutation(*test_strings)
            self.assertTrue(result)
        # false check
        for test_strings in self.dataF:
            result = checkPermutation(*test_strings)
            self.assertFalse(result)

if __name__=="__main__":
    unittest.main()