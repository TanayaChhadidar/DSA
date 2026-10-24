class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Lqueue:
    def __init__(self):
        self.front = None
        self.rear = None
    def enqueue(self, data):
        NewNode = Node(data)
        if self.rear != None:
            self.rear.next = NewNode
            self.rear = NewNode
        else:
            self.front = self.rear = NewNode
    def dequeue(self):
        curr = self.front
        print("Deleted node: ", curr.data)
        self.front = self.front.next
        if self.front == None:
            print("Queue is empty")
            self.rear = None
        curr = None
    def printqueue(self):
        curr = self.front
        while curr:
            print(curr.data, end=" ")
            curr = curr.next
        print()
que = Lqueue()
que.enqueue(10)
que.enqueue(11)
que.enqueue(12)
que.enqueue(13)
que.printqueue()
que.dequeue()
que.dequeue()
que.dequeue()
que.dequeue()

que.printqueue()