import unittest

def urlify(word, length):
    # O(n)
    toAdd = "%20"
    result = ""
    stringSplit = word.strip().split(' ')
    # Add all string but last
    for i in range(len(stringSplit)-1):
        result += stringSplit[i] + toAdd

    return result + stringSplit[len(stringSplit)-1]

# Better solution with less space. But the string input is already in an array. String is returned and not creating a new string
def urlify1(string, length):
    # Length is true length of string 'Hello, mr sir'
    # Function replaces single spaces with %20 and removes trailing spaces
    new_index = len(string)
    print("first:\n", string)

    for i in reversed(range(length)):
        if string[i] == ' ':
            # replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index - 1] = string[i]
            new_index -= 1
        print(string)
    
    return string

class Test(unittest.TestCase):
    # Using lists because Python strings are immutable
    # data = [
    #     (list('much ado about nothing      '), 22,
    #      list('much%20ado%20about%20nothing')),
    #     (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))]
    data = [
    (list('Mr John Smith    '), 13, list('Mr%20John%20Smith')),
    (list('Hello Mr Sir   '), 12, list('Hello%20Mr%20Sir'))
    ]
    

    def test_urlify(self):
        for [test_string, length, expected] in self.data:
            actual = urlify1(test_string, length)
            self.assertEqual(actual, expected)

    def test_urlify1(self):
        result = urlify('much ado about nothing      ', 22)
        self.assertEqual(result, 'much%20ado%20about%20nothing')

if __name__=="__main__":
    unittest.main()