def merge_lists(list1, list2):
    newList = []
    l1 = 0
    l2 = 0
    while l1 < len(list1) and l2 < len(list2):
        if list1[l1] < list2[l2]:
            newList.append(list1[l1])
            l1 += 1
        else:
            newList.append(list2[l2])
            l2 += 1
    
    while l1 < len(list1):
        newList.append(list1[l1])
        l1 += 1
    
    while l2 < len(list2):
        newList.append(list2[l2])
        l2 += 1
    
    return newList

def main():
    my_list     = [3, 4, 6, 10, 11, 15]
    alices_list = [1, 5, 8, 12, 14, 19]

    # Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
    print(merge_lists(my_list, alices_list))

main()