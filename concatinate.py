def concatenate_lists(list1, list2):
    if list1 is None:
        return list2
    if list2 is None:
        return list1

    current = list1
    while current.next:
        current = current.next
    current.next = list2

    return list1