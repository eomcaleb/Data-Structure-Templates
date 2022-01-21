from data_structures.binarytree import BinaryTree, Node

def main():    
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

if __name__ == "__main__":
    main()

