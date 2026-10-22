class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        return self.top is None
    def push(self, new_node ):
        new_node.next = self.top
        self.top = new_node
    def print(self):
        print("Stack Contents:")
        temp= self.top
        while temp:
            print(temp.data)
            temp = temp.next
st=Stack()
st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.push(Node(50))
st.print()