# O(n^2) solution, my solution
def minimumSwaps1(arr):
    sortedArr = sorted(arr)
    correctIndex = {}
    for i in range(len(sortedArr)):
        correctIndex[sortedArr[i]] = i

    isSorted = False
    swapCount = 0
    while not isSorted:
        isSorted = True
        for i in range(len(arr)):
            currentNum = arr[i]
            toIndex = correctIndex[currentNum]
            if i != toIndex:
                arr[i], arr[toIndex] = arr[toIndex], arr[i]
                swapCount += 1
                isSorted = False

    return swapCount

# Improved hash map solution O(n)
def minSwap2(arr):
    n = len(arr)
    countSwaps = 0
    hIndex = {}
    temp = sorted(arr)

    # Keep track of original array indexes
    for i in range(n):
        hIndex[arr[i]] = i
    
    init = 0
    for i in range(n):
        # elements do not match
        if (arr[i] != temp[i]):
            countSwaps += 1
            # store curr arr element
            init = arr[i]

            # If arr and temp don't match, swap this element
            # with the index of the element which should come here
            arr[i], arr[hIndex[temp[i]]] = arr[hIndex[temp[i]]], arr[i]

            # Update the indexes in the hashmap accordingly
            hIndex[init] = hIndex[temp[i]]
            hIndex[temp[i]] = i
            print("Updated arr:", arr)
            print("Updated hIndex:", hIndex)
    
    return countSwaps

# Graph swap
def minSwap3(arr):
    n = len(arr)

    # temp array: index position, value
    arrpos = [*enumerate(arr)]
    # sorting arrpos by value
    arrpos.sort(key = lambda it: it[1])

    # Keep track of visited elements starting with all false
    vis = {k: False for k in range(n)}

    swapCount = 0
    for i in range(n):
        # Current i is:
        # already swapped or already present at correct position
        if vis[i] or arrpos[i][0] == i:
            continue

        # find number of nodes in this cycle and add it to swapCount
        cycle_size = 0
        j = i

        while not vis[j]:
            # mark node as visited
            vis[j] = True

            # move to next node
            j = arrpos[j][0]
            cycle_size += 1
        
        # update answer by adding current cycle
        if cycle_size > 0:
            swapCount += (cycle_size - 1)

    return swapCount

def main():
    a = [4,3,1,2]
    print(minSwap3(a))
    print(a)

main()