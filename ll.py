class LinkedList:

 def delete_first_last(head):    
    if head is None or head.next is None:
        return None

    # Delete the first node
    head = head.next

    # Delete the last node
    current = head
    while current.next and current.next.next:
        current = current.next
    current.next = None

    return head