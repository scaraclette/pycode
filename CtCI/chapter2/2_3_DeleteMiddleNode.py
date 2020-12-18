# Implement an algorithm to delete a node in the middle of a singly linked list. The start of the node is the given linked list.

from LinkedList import LinkedList

def delete_middle_node(middle):
    middle.value = middle.next.value
    middle.next = middle.next.next
    

ll = LinkedList()
ll.add_multiple([1, 2, 3, 4])
middle_node = ll.add(5)
ll.add_multiple([7, 8, 9])

print(ll)
delete_middle_node(middle_node)
print(ll)