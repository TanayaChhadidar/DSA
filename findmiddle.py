def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow.data

#delete the middle element of a list    
def delete_middle(head):
    if head is None or head.next is None:
        return None

    slow = head
    fast = head
    prev = None

    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Delete the middle node
    prev.next = slow.next

    return head