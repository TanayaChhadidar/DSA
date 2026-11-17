
# Stack Implementation

stack = []

def push():
    element = int(input("Enter element: "))
    stack.append(element)
    print("Element pushed successfully")

def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Popped element:", stack.pop())

def display():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        print("Stack elements:", stack)

def reverse_string():
    string = input("Enter a string: ")
    temp = []

    for ch in string:
        temp.append(ch)

    reverse = ""
    while len(temp) > 0:
        reverse += temp.pop()

    print("Reversed string:", reverse)

def reverse_stack():
    temp = []

    while len(stack) > 0:
        temp.append(stack.pop())

    while len(temp) > 0:
        stack.append(temp.pop())

    print("Reversed stack:", stack)


while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Reverse String using Stack")
    print("5. Reverse Stack using another Stack")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        reverse_string()
    elif choice == 5:
        reverse_stack()
    elif choice == 6:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
