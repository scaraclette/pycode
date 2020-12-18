def permutationPalindrome(word):
    dictLetter = {}
    for i in word:
        dictLetter[i] = dictLetter.get(i, 0) + 1
    
    middle = False
    for key in dictLetter:
        if dictLetter[key] % 2 != 0:
            if middle:
                return False
            else:
                middle = True

    return True

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    return len(unpaired_characters) <= 1

def main():
    w1 = "civic"
    w2 = "madam"
    w3 = "ccxiiixcc"
    print(permutationPalindrome(w3))

main()