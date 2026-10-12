class Node:
   
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        
        new_node = Node(val)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def print_list(self):
        
        if not self.head:
            print("List is empty.")
            return
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(output) + " -> None")

    def insert_at_position(self, val, position):
        
        new_node = Node(val)
        
        if position == 1:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for _ in range(1, position - 1):
            if temp is None:
                break
            temp = temp.next

        if temp is None:
            print("Position out of bounds.")
        else:
            new_node.next = temp.next
            temp.next = new_node

    def print_middle(self):
        
        if not self.head:
            print("List is empty, no middle node.")
            return
        
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        print(f"Middle node value: {slow.data}")

    def delete_node(self, val):
        
        if not self.head:
            return

        if self.head.data == val:
            self.head = self.head.next
            return

        temp = self.head
        while temp.next and temp.next.data != val:
            temp = temp.next

        if temp.next is None:
            print(f"Value {val} not found in the list.")
        else:
            temp.next = temp.next.next

    def reverse_list(self):
        
        prev = None
        current = self.head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def sum_consecutive_pairs(self):
        
        if not self.head or not self.head.next:
            print("Not enough elements to calculate consecutive sums.")
            return
        
        temp = self.head
        sums = []
        while temp and temp.next:
            pair_sum = temp.data + temp.next.data
            sums.append(str(pair_sum))
            temp = temp.next.next  
            
        print("Consecutive Sums: " + " ".join(sums))


if __name__ == "__main__":
    llist = LinkedList()

   
    llist.insert_at_end(10)
    llist.insert_at_end(20)
    llist.insert_at_end(30)
    llist.insert_at_end(40)
    llist.insert_at_end(50)

    print("Original List:")
    llist.print_list()

    
    print("\nInserting 25 at position 3:")
    llist.insert_at_position(25, 3)
    llist.print_list()

    
    llist.print_middle()

    
    print("\nDeleting node with value 30:")
    llist.delete_node(30)
    llist.print_list()

    
    llist.sum_consecutive_pairs()

    
    print("\nReversing the list:")
    llist.reverse_list()
    llist.print_list()
