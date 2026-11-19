class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class Hospital:
    def __init__(self):
        self.front = None

    # Add Patient
    def enqueue(self, new_node):
        if self.front == None:
            self.front = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
            return

        temp = self.front

        while temp.next != None and temp.next.priority <= new_node.priority:
            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node

    # Display Next Patient
    def display_next(self):
        if self.front == None:
            print("Queue is empty")
        else:
            print("Next Patient:", self.front.name)

    # Remove Patient
    def dequeue(self):
        if self.front == None:
            print("Queue is empty")
        else:
            temp = self.front
            print("Treated Patient:", temp.name)
            self.front = self.front.next

    # Display All Patients
    def display_all(self):
        if self.front == None:
            print("Queue is empty")
            return

        temp = self.front

        while temp != None:
            print(temp.pid, temp.name, temp.priority)
            temp = temp.next



h = Hospital()

h.enqueue(Node(101, "Tanaya", 3))
h.enqueue(Node(102, "Atharv", 1))
h.enqueue(Node(103, "Sonal", 2))

print("All Waiting Patients:")
h.display_all()

print("\nNext Patient:")
h.display_next()

print("\nAfter Treatment:")
h.dequeue()

print("\nRemaining Patients:")
h.display_all()