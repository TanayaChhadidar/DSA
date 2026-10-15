class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_node):
        temp = self.head
        if temp:
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = new_node
        else:
            self.head = new_node
    def print(self):
        temp = self.head
        print("List elements: ")
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
list1 = LinkedList()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.print()