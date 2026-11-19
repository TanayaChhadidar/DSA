class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BST:
    def __init__(self):
        self.root = None

    def insert(self, newnode):
        if self.root is None:
            self.root = newnode
            return

        else:
            temp = self.root

            while True:
                if newnode.value > temp.value:
                    if temp.right is None:
                        temp.right = newnode
                        return
                    else:
                        temp = temp.right

                elif newnode.value < temp.value:
                    if temp.left is None:
                        temp.left = newnode
                        return
                    else:
                        temp = temp.left

                else:
                    print("Duplicate value not allowed")
                    return

    # inorder traversal
    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)


# main program
biny = BST()

biny.insert(Node(10))
biny.insert(Node(20))
biny.insert(Node(30))
biny.insert(Node(5))
biny.insert(Node(15))

print("Inorder Traversal:")
biny.inorder(biny.root)