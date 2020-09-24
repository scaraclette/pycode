# DUPLICATE ZEROS
# Given a fixed length array arr of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.
# Example [1,0,2,3,0,4,5,0] -> [1,0,0,2,3,0,0,4]
def duplicateZeros():
    A = [1,0,2,3,0,4,5,0]
    print(id(A))

    index = 0
    while index < len(A):
        if A[index] == 0:
            # add 0 after current index
            A.insert(index, 0)
            # remove last digit from A
            A.pop()
            # increment index to avoid new 0
            index += 2
        else:
            index += 1
    
    print(id(A))


duplicateZeros()