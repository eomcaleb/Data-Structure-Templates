from data_structures.singlylinkedlist import SingleLinkedList

def main():
    sl = SingleLinkedList()
    sl.insert(1)
    sl.insert(2)
    sl.insert(3)

    # Print
    sl.print()

    # Size
    print("Size: ", sl.count(), " node(s) found.") 

    # Pop
    sl.pop()

    # Search
    print("Searching for node 2 in the SLL: ", sl.search(1))

    # Delete
    sl.delete(3)
    sl.print()

    # InsertPosition
    sl.insertposition(4,1)
    sl.print()

    # Clear
    sl.clear()

    # InsertBack
    sl.insertback(22)
    sl.print()

    # Delete Occurance
    sl.insert(22)
    sl.insert(22)
    sl.insert(223)
    sl.insert(22)
    sl.insert(22)
    sl.print()
    sl.deleteoccurance(22)
    sl.print()

if __name__ == "__main__":
    main()

