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

    # Breadth First Search algorithm start from top and move down each height
    def breadthfirstprint(self, start):
        if start:
            queue = [start]
            while queue:
                node = queue.pop(0)
                if node:
                    print(node.data, end = ' ')
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
    
    # Depth First Search algorithm traverses a tree down one path first
    def depthfirstprint(self, start, type):
        if type == "Pre-Order":
            print(self.preorder(start, ""))
        elif type == "In-Order":
            print(self.preorder(start, ""))
        elif type == "Post-Order":
            print(self.preorder(start, ""))


    def preorder(self, start, traversal):
        if start:
            traversal += (str(start.data) + " ")
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        return traversal
    
    def inorder(self, start, traversal):
        if start:
            traversal = self.inorder(start.left, traversal)
            traversal += (str(start.data) + " ")
            traversal = self.inorder(start.right, traversal)
        return traversal    
    
    def postorder(self, start, traversal):
        if start:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal += (str(start.data) + " ")
        return traversal

