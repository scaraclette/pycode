"""
#20: You can do this in O(A+B) time and 0(1) additional space. That is, you do not need a hash table (although you could do it with one).
#45: Examples will help you. Draw a picture of intersecting linked lists and two equivalent
linked lists (by value) that do not intersect.
#55: Focus first on just identifying if there's an intersection.
#65: Observe that two intersecting linked lists will always have the same last node. Once they intersect, all the nodes after that will be equal.
#76
#93
#111
#120
#129
"""
from LinkedList import LinkedList

def intersection(list1: LinkedList, list2: LinkedList):
    if list1.tail is not list2.tail:
        return False
    
    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next
    
    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node

