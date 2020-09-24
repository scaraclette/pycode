def shuffleArray(a, n):
    n = n // 2
  
    start = n + 1
    j = n + 1
    for done in range( 2 * n - 2) : 
        if (start == j) : 
            start -= 1
            j -= 1
  
        i = j - n if j > n else j 
        j = 2 * i if j > n else 2 * i - 1
  
        a[start], a[j] = a[j], a[start]

# Driver code
def main():
    a = [1, 2, 3, 'a', 'b', 'c']
    n = len(a)

    shuffleArray(a, n)
    print(a)

main()