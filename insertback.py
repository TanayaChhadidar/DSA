def insert_at_end(head, new_node):
    if head is None:
        head = new_node
        return head
    current = head
    while current.next:     
        current = current.next      
    current.next = new_node
    return head