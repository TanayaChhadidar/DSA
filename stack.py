class Node:
    def __init__(self, value):
        self.data= value
        self.next = None

class stack:
    def __init__(self):
        self.top = None
    def isempty(self):
        if self.top is None:
            return True
        return False
    def push(self,new_node):
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return
        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        return popped_node.data
    def print(self):
        print("Stack elements are:")
        if self.isempty():
            print("Stack is empty")
            return    
        else:
            temp = self.top
            while temp:
                print(temp.data)
                temp=temp.next
    def reverse(self):
        temp=self.top
        while temp:
            new_node = Node(temp.data)
            st1.push(new_node)
            temp=temp.next    
st = stack()
st1 = stack()

st.push(Node(10))
st.push(Node(20))
st.push(Node(30))
st.push(Node(40))
st.print()
st.pop()

st.print()
st.reverse()
st.print()