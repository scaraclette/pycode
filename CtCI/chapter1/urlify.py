import unittest

def urlify(word, length):
    myList = [i for i in word]
    index = len(word) - 1
    # print("Index:", myList[index])
    while length > 0:
        curr = length - 1
        if myList[curr] != ' ':
            myList[index] = myList[curr]
            index -= 1
        elif myList[curr] == ' ':
            myList[index] = '0'
            index -= 1
            myList[index] = '2'
            index -= 1
            myList[index] = '%'
            index-= 1
        length -= 1

    return myList

def urlify1(word, length):
    word.strip()
    print(word)
    result = word.split()
    word = "%20".join(result)
    return [i for i in word]

class Test(unittest.TestCase):
    '''Test Cases'''
    # Using lists because Python strings are immutable
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify(test_string, length)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
# print(urlify('Mr John Smith    ', 13))
# print(urlify1('much ado about nothing      ', 22))
# print(list('Mr%20John%20Smith'))