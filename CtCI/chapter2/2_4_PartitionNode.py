"""
    HINTS
#3: Many solutions to this problem, most of which are equally optimal in runtime.
    Some have shorter, cleaner code than others. Can you brainstorm different solutions?
#24:
"""
from LinkedList import LinkedList

def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        nextNode = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = nextNode
        
    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


ll = LinkedList()
ll.add(1)
ll.add(4)
ll.add(3)
ll.add(2)
ll.add(5)
ll.add(2)
print(ll)
partition(ll, 3)
print(ll)