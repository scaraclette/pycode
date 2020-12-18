"""
Hints
8: What if you knew the linked list size? What is the difference between finding  the Kth-to-last element and finding the Xth element?
25: If you don't know the linked list size, can you compute it? How does this impact the runtime?
41:
67:
126:
"""
from LinkedList import LinkedList

def kth_to_last(ll, n):
    curr = ll.head
    count = 0
    while curr:
        count += 1
        curr = curr.next
    
    toFind = count - n
    print("toFind:", toFind)
    curr = ll.head
    while toFind > 0:
        print(toFind, curr.value)
        curr = curr.next
        toFind -= 1

    return curr.value

def kth_to_last_1(ll, k):
    runner = curr = ll.head
    for _ in range(k):
        if runner is None:
            return None
        runner = runner.next
    
    print(runner.value)
    
    while runner:
        curr = curr.next
        runner = runner.next
    
    return curr

ll = LinkedList()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)
ll.add(5)

print(ll)
print(kth_to_last_1(ll, 2))