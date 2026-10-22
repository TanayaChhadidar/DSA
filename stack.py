class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        if self.top == None:
            return self.top is None
    def push(self, data):
        NewNode = Node(data)
        if self.isempty():
            self.top = NewNode
            NewNode = self.top
        else:
            NewNode.next = self.top
            self.top = NewNode
        
    def pop(self):
        if self.isempty():
            print("Stack is Underflow")
        else:
            curr = self.top
            self.top = self.top.next
            curr = None
    def print_stack(self):
        curr = self.top
        while curr != None:
            print(curr.data, end=" ")
            curr = curr.next
        print()
    def reverse(self):
        curr = self.top
        while curr:
            NewStack.push(Node(curr.data))
            prev = curr
            curr = curr.next
        return prev
stack = stack()
NewStack = stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.print_stack()
stack.pop()
stack.print_stack()
NewStack.reverse()