from LinkedList import LinkedList

def sum_lists(l1, l2):
    result = LinkedList()
    carry = 0
    while l1 and l2:
        currentSum = l1.value + l2.value
        if currentSum > 9 and carry == 0:
            result.add(currentSum - 10)
            carry = 1
        elif carry != 0 and currentSum + carry < 10:
            result.add(currentSum + 1)
            carry = 0
        elif carry != 0 and currentSum + carry > 9:
            result.add(currentSum + 1 - 10)
        else: # carry == 0 and currentSum < 10
            result.add(currentSum)

        l1 = l1.next
        l2 = l2.next
    
    if carry != 0:
        result.add(1)

    return result

def sum_lists_followup(ll_a, ll_b):
    # Pad the shorter list with zeros
    if len(ll_a) < len(ll_b):
        for i in range(len(ll_b) - len(ll_a)):
            ll_a.add_to_beginning(0)
    else:
        for i in range(len(ll_a) - len(ll_b)):
            ll_b.add_to_beginning(0)
    
    # Find sum
    n1, n2 = ll_a.head, ll_b.head
    result = 0
    while n1 and n2:
        result = (result * 10) + n1.value + n2.value
        n1 = n1.next
        n2 = n2.next
    
    ll = LinkedList()
    ll.add_multiple([int(i) for i in str(result)])

    return ll

ll1 = LinkedList()
ll1.add(2)
ll1.add(4)
ll1.add(3)
ll2 = LinkedList()
ll2.add(5)
ll2.add(6)
ll2.add(4)
print(ll1, "+", ll2)
print(sum_lists_followup(ll1.head, ll2.head))