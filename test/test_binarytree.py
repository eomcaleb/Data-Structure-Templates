from data_structures.binarytree import BinaryTree, Node

def main():    
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    
    print("Breadth First Print")
    tree.breadthfirstprint(tree.root)
    print("\n")

    print("Depth First Print - PreOrder")
    tree.depthfirstprint(tree.root, "Pre-Order")
    
    print("Depth First Print - InOrder")
    tree.depthfirstprint(tree.root, "In-Order")
    
    print("Depth First Print - PostOrder")
    tree.depthfirstprint(tree.root, "Post-Order")

if __name__ == "__main__":
    main()

