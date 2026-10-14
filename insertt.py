#singly circular linked list
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
class SCL:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.tail.next = self.head

    def display(self):
        if not self.head:
            return "List is empty"
        current = self.head
        result = []
        while True:
            result.append(current.data)
            current = current.next
            if current == self.head:
                break
        return result
    
list1 = SCL()
list1.insert(1)
list1.insert(2)
print(list1.display())