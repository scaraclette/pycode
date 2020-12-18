def reverseString(word):
    n = len(word)
    for i in range(n // 2):
        word[i], word[n-1-i] = word[n-1-i], word[i]

def main():
    s1 = ["h", "e", "l", "l", "o"]
    reverseString(s1)
    print(s1)

main()