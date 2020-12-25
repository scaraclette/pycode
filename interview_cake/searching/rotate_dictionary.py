def indexStart(words):
    low = 0
    high = len(words) - 1
    previousWord = words[0]

    while low < high:
        mid = low + (high - low) // 2
        currentWord = words[mid]
        if currentWord < previousWord:
            previousWord = currentWord
            high = mid
        else:
            previousWord = currentWord
            low = mid + 1
    
    return low

def solution(words):
    firstWord = words[0]
    floorIndex = 0
    ceilingIndex = len(words) - 1
    while floorIndex < ceilingIndex:
        # Guess a point halfway between floor and ceiling 
        guessIndex = floorIndex + (ceilingIndex - floorIndex) // 2

        # If guess comes after first word or is the first word
        if words[guessIndex] >= firstWord:
            # Go right
            floorIndex = guessIndex
        else:
            ceilingIndex = guessIndex
        
        # If floor and ceiling have converged
        if floorIndex + 1 == ceilingIndex:
            return ceilingIndex


def main():
    words1 = ['o', 'p', 'q', 'r', 's', 't', 'u', 'a', 'b']
    words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'alit',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
    ]

    indexAt = indexStart(words1)
    print(words1[indexAt])

main()