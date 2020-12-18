def checker(takeOut, dineIn, served):
    tPointer = 0
    dPointer = 0

    print(len(served))
    print(len(takeOut) + len(dineIn))
    if len(served) > (len(takeOut) + len(dineIn)):
        return False

    for i in served:
        if tPointer < len(takeOut) and i == takeOut[tPointer]:
            tPointer += 1
        elif dPointer < len(dineIn) and i == dineIn[dPointer]:
            dPointer += 1
        else:
            return False
    

    return True

def main():
    TO1 = [1, 3, 5]
    DI1 = [2,4,6]
    served1 = [1,2,4,6,5,3]
    print(checker(TO1, DI1, served1) == False)

    t2 = [17,8,24]
    d2 = [12,19,2]
    s2 = [17, 8, 12, 19, 24, 2]
    print(checker(t2, d2, s2) == True)

    t3 = [17,8,24]
    d3 = [12,19,2]
    s3 = [17, 8, 12, 19, 24, 2, 100]
    print(checker(t3, d3, s3) == False)

main()
