# Binary Tree
# ------------
# A type of linked list that has at 2 nodes maximum per node (left and right) 

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)

    def print_preorder(self, start, traversal):
        if start:
            traversal += (str(start.data) + "-")
            traversal = self.print_preorder(start.left, traversal)
            traversal = self.print_preorder(start.right, traversal)
        return traversal
    
    def print_inorder(self, start, traversal):
        if start:
            traversal = self.print_inorder(start.left, traversal)
            traversal += (str(start.data) + "-")
            traversal = self.print_inorder(start.right, traversal)
        return traversal
    
    
    def print_postorder(self, start, traversal):
        if start:
            traversal = self.print_postorder(start.left, traversal)
            traversal = self.print_postorder(start.right, traversal)
            traversal += (str(start.data) + "-")
        return traversal


tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.print_preorder(tree.root, ""))
print(tree.print_inorder(tree.root, ""))
print(tree.print_postorder(tree.root, ""))